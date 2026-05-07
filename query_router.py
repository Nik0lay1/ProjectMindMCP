"""
Tier-aware query router.

Tier escalation policy:
  L0 (manifest)   — paths + symbols. Always tried first. ~50 ms.
  L1 (BM25)       — keyword/lexical. Loaded only when L0 is insufficient.
  L2 (vector)     — semantic. Loaded only on explicit semantic intent or
                    when L0+L1 produced nothing useful.

Intents:
  "overview"  -> L0 only
  "lookup"    -> L0 then L1
  "semantic"  -> L0 then L1 then L2
  "deep"      -> L0 then L1 then L2 with relaxed thresholds and more results
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import config
from logger import get_logger

logger = get_logger()


VALID_INTENTS = ("overview", "lookup", "semantic", "deep")


@dataclass
class QueryHit:
    source: str
    score: float
    tier: str
    snippet: str = ""
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "score": round(self.score, 3),
            "tier": self.tier,
            "snippet": self.snippet,
            "extra": self.extra,
        }


@dataclass
class QueryResult:
    query: str
    intent: str
    hits: list[QueryHit]
    tiers_used: list[str]
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "intent": self.intent,
            "tiers_used": self.tiers_used,
            "hit_count": len(self.hits),
            "hits": [h.to_dict() for h in self.hits],
            "notes": self.notes,
        }

    def to_markdown(self) -> str:
        lines = [
            f"# QUERY: {self.query}",
            f"**Intent**: {self.intent}",
            f"**Tiers used**: {', '.join(self.tiers_used) or 'none'}",
            f"**Hits**: {len(self.hits)}",
            "",
        ]
        if self.notes:
            lines.append("## Notes")
            for n in self.notes:
                lines.append(f"- {n}")
            lines.append("")
        for i, h in enumerate(self.hits, 1):
            lines.append(f"## {i}. `{h.source}` _(tier={h.tier}, score={h.score:.2f})_")
            if h.snippet:
                lines.append("```")
                lines.append(h.snippet[:1200])
                lines.append("```")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Tier handlers
# ---------------------------------------------------------------------------


def _tier_l0(query: str, n: int) -> list[QueryHit]:
    from manifest import find_files_by_keyword, get_or_build_manifest

    try:
        m = get_or_build_manifest()
    except Exception as e:
        logger.warning(f"L0 manifest load failed: {e}")
        return []
    entries = find_files_by_keyword(m, query, limit=n)
    hits: list[QueryHit] = []
    for entry in entries:
        snippet = ", ".join(entry.symbols[:8]) if entry.symbols else ""
        hits.append(
            QueryHit(
                source=entry.path,
                score=1.0,
                tier="L0",
                snippet=snippet,
                extra={"size": entry.size, "lang": entry.lang},
            )
        )
    return hits


def _tier_l1(query: str, n: int) -> list[QueryHit]:
    """BM25 / keyword. Loads BM25 index but NOT the embedding model."""
    try:
        from bm25_index import BM25Index
    except Exception as e:
        logger.warning(f"BM25 unavailable: {e}")
        return []
    try:
        idx = BM25Index(config.BM25_INDEX_PATH)
        idx.load()
        if not idx.is_ready:
            return []
        items = idx.search(query, n=n)
    except Exception as e:
        logger.warning(f"BM25 search failed: {e}")
        return []
    hits: list[QueryHit] = []
    for it in items:
        meta = it.get("metadata") or {}
        hits.append(
            QueryHit(
                source=meta.get("source") or it.get("id", ""),
                score=float(it.get("score", 0.0)),
                tier="L1",
                snippet=(it.get("text") or "")[:600],
                extra={"id": it.get("id")},
            )
        )
    return hits


def _tier_l2(query: str, n: int) -> list[QueryHit]:
    """Semantic vector search. Loads embedding model on first use."""
    try:
        from context import get_context

        ctx = get_context()
        vs = ctx.vector_store
        coll = vs.get_collection()
        if coll is None:
            return []
        raw = vs.hybrid_query(query_texts=[query], n_results=n)
    except Exception as e:
        logger.warning(f"L2 vector query failed: {e}")
        return []
    if not raw or not raw.get("ids") or not raw["ids"][0]:
        return []
    hits: list[QueryHit] = []
    ids = raw["ids"][0]
    docs = (raw.get("documents") or [[]])[0]
    metas = (raw.get("metadatas") or [[]])[0]
    distances = (raw.get("distances") or [[]])[0]
    for i, doc_id in enumerate(ids):
        meta = metas[i] if i < len(metas) else {}
        dist = distances[i] if i < len(distances) else 0.0
        score = max(0.0, 1.0 - float(dist))
        hits.append(
            QueryHit(
                source=meta.get("source", doc_id),
                score=score,
                tier="L2",
                snippet=(docs[i] if i < len(docs) else "")[:800],
                extra={"id": doc_id, "distance": dist},
            )
        )
    return hits


# ---------------------------------------------------------------------------
# Merging
# ---------------------------------------------------------------------------


def _merge_hits(buckets: list[list[QueryHit]], limit: int) -> list[QueryHit]:
    seen: dict[str, QueryHit] = {}
    for bucket in buckets:
        for h in bucket:
            key = h.source
            existing = seen.get(key)
            if existing is None:
                seen[key] = h
            elif h.score > existing.score:
                seen[key] = h
    ordered = sorted(seen.values(), key=lambda x: x.score, reverse=True)
    return ordered[:limit]


def query(
    user_query: str,
    intent: str = "lookup",
    n_results: int = 8,
) -> QueryResult:
    """
    Routes a user query through the appropriate tiers.

    Args:
        user_query: Free-form query text
        intent: One of "overview" | "lookup" | "semantic" | "deep"
        n_results: Final number of hits to return
    """
    if not user_query or not user_query.strip():
        return QueryResult(
            query=user_query,
            intent=intent,
            hits=[],
            tiers_used=[],
            notes=["empty query"],
        )

    intent = intent.strip().lower()
    if intent not in VALID_INTENTS:
        intent = "lookup"

    tiers_used: list[str] = []
    notes: list[str] = []
    buckets: list[list[QueryHit]] = []

    # L0
    l0 = _tier_l0(user_query, n=max(n_results * 2, 12))
    if l0:
        tiers_used.append("L0")
        buckets.append(l0)

    if intent == "overview":
        merged = _merge_hits(buckets, n_results)
        if not merged:
            notes.append("no L0 matches; try a more specific keyword")
        return QueryResult(user_query, intent, merged, tiers_used, notes)

    # Decide whether to escalate to L1
    need_more = intent in ("semantic", "deep") or len(l0) < max(3, n_results // 2)
    if need_more:
        l1 = _tier_l1(user_query, n=max(n_results * 2, 12))
        if l1:
            tiers_used.append("L1")
            buckets.append(l1)
        elif intent == "lookup":
            notes.append("BM25 index empty; run `index_codebase()` for keyword search")

    # Decide whether to escalate to L2
    if intent in ("semantic", "deep"):
        merged_so_far = _merge_hits(buckets, n_results)
        weak_signal = not merged_so_far or merged_so_far[0].score < 0.4 or intent == "deep"
        if weak_signal:
            l2_n = max(n_results * 2, 12) if intent == "deep" else n_results
            l2 = _tier_l2(user_query, n=l2_n)
            if l2:
                tiers_used.append("L2")
                buckets.append(l2)
            else:
                notes.append("vector tier unavailable; index may be empty")

    final = _merge_hits(buckets, n_results)
    if not final:
        notes.append(
            "no hits across L0/L1/L2 — index might be missing; "
            "try `index_codebase()` or refine the query"
        )
    return QueryResult(user_query, intent, final, tiers_used, notes)

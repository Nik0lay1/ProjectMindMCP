# ProjectMind MCP

> Give your AI coding assistant a brain. Persistent memory, semantic code search, and project intelligence — all running locally with no API keys required.

**ProjectMind** is an open-source [MCP (Model Context Protocol)](https://modelcontextprotocol.io) server that supercharges AI assistants like Claude, Zencoder, and Cursor with long-term project memory and intelligent codebase search.

> 🤖 **This project was built with AI** — designed, coded, debugged, and documented using AI-assisted development from day one.

---

## Why ProjectMind?

Every time you start a new AI session, your assistant forgets everything about your project. ProjectMind solves this:

- **No more re-explaining** your architecture every session
- **Semantic code search** that understands *what* code does, not just *what* it's named
- **Dependency graph analysis** to understand how modules connect
- **Works 100% locally** — your code never leaves your machine

---

## Features

### 🧠 Persistent Project Memory
Save architectural decisions, tech stack notes, and context that survives across sessions. The AI reads this at the start of every conversation.

### 🔍 Semantic Code Search
Search your codebase by *meaning*, not just text. Powered by a local `sentence-transformers` model — no OpenAI key needed.

```
"find authentication middleware"  →  finds auth code even if it's named differently
```

### 🌳 AST-Aware Chunking
Unlike naive text splitters that cut code in the middle of a function, ProjectMind uses [tree-sitter](https://tree-sitter.github.io) to parse source files into **exact syntax units**:

- Functions and methods are indexed as individual, self-contained chunks
- Class methods get a `# Class: ClassName` context prefix for better search relevance
- Rich metadata per chunk: `symbol_type`, `symbol_name`, `class_name`, `line_start`, `line_end`
- Supports: **Python, JavaScript, TypeScript, TSX, Java, Go, Rust, Ruby**
- Graceful fallback to text splitting for unsupported file types

### 🕸 Dependency Graph Intelligence
- Traverse import relationships up to 5 levels deep
- Find related files via shared dependency clustering
- Discover the shortest path between any two modules
- Identify entry points and orphaned modules
- **Cached import graph** (120s TTL) — repeated calls return instantly instead of re-scanning the filesystem

### ⚡ Instant Project Exploration (no indexing needed)
- `get_project_overview()` — tech stack, git info, file stats in < 1 second
- `explore_directory(path)` — browse project tree level by level
- `get_file_summary(path)` — imports, classes, functions, git history

### ⚡ Hybrid Search (BM25 + Vector)
Two search engines combined via **Reciprocal Rank Fusion (RRF)**:
- **BM25** catches exact keyword matches — finds `getUserById` when you type exactly that
- **Vector search** catches semantic matches — finds auth code even if named differently
- RRF merges both ranked lists for best-of-both-worlds results
- Automatic fallback to pure vector search when BM25 index is not ready

### 🔄 Incremental Indexing
Only re-indexes changed files — 10-100x faster than full re-indexing.

### 📊 Code Quality Metrics
Cyclomatic complexity, pylint scores, test coverage tracking — all queryable via MCP tools.

---

## Quick Start

### 1. Clone and install

```bash
git clone https://github.com/Nik0lay1/project-mind-mcp.git
cd project-mind-mcp
python -m venv .venv

# Windows
.venv\Scripts\pip install -e .

# macOS/Linux
.venv/bin/pip install -e .
```

### 2. Add to your MCP client

**Zencoder / Claude Desktop** — add to `mcp.json`:

```json
{
  "mcpServers": {
    "Memory": {
      "command": "/path/to/ProjectMindMCP/.venv/bin/python",
      "args": ["/path/to/ProjectMindMCP/mcp_server.py"]
    }
  }
}
```

**Windows example:**
```json
{
  "mcpServers": {
    "Memory": {
      "command": "F:\\Projects\\ProjectMindMCP\\.venv\\Scripts\\python.exe",
      "args": ["F:\\Projects\\ProjectMindMCP\\mcp_server.py"]
    }
  }
}
```

### 3. Index your project

In your target project, ask the AI:
```
Memory__index_codebase
```

Or run directly for large projects:
```bash
# Windows
.venv\Scripts\python.exe run_index.py

# macOS/Linux
.venv/bin/python run_index.py
```

---

## Available Tools (40+)

| Category | Tools |
|---|---|
| **Memory** | `read_memory`, `update_memory`, `clear_memory`, `save_memory_version` |
| **Search** | `search_codebase`, `search_for_feature`, `search_architecture`, `search_for_errors` |
| **Exploration** | `get_project_overview`, `explore_directory`, `get_file_summary` |
| **Dependencies** | `get_file_relations`, `get_dependencies_with_depth`, `get_module_cluster`, `find_dependency_path` |
| **Indexing** | `index_codebase`, `index_changed_files`, `get_index_stats` |
| **Git** | `ingest_git_history`, `get_recent_changes_summary`, `auto_update_memory_from_commits` |
| **Quality** | `analyze_code_complexity`, `analyze_code_quality`, `get_test_coverage_info` |
| **Project** | `set_project_root`, `detect_project_conventions`, `generate_project_summary` |

Full reference: [docs/api/tools-reference.md](docs/api/tools-reference.md)

---

## How It Works

```
Your Project
     │
     ▼
ProjectMind MCP Server
     │
     ├── .ai/memory.md          ← persistent notes & decisions
     ├── .ai/vector_store/      ← ChromaDB embeddings (local)
     └── .ai/index_metadata.json ← tracks changed files
     │
     ▼
AI Assistant (Claude / Zencoder / Cursor)
```

**Embedding model**: `flax-sentence-embeddings/st-codesearch-distilroberta-base`
- Trained specifically on code (CodeSearchNet dataset)
- ~130MB, runs fully locally on CPU
- No API keys, no data sent anywhere

**Search pipeline**: BM25 (keyword) + ChromaDB (semantic) → Reciprocal Rank Fusion → top-N results

---

## Requirements

- Python 3.10 – 3.12
- ~500MB disk (model + dependencies)
- Works on Windows, macOS, Linux

---

## Configuration

All settings in `config.py`:

| Setting | Default | Description |
|---|---|---|
| `MODEL_NAME` | `flax-sentence-embeddings/st-codesearch-distilroberta-base` | Embedding model |
| `CHUNK_SIZE` | `1500` | Characters per chunk |
| `MAX_FILE_SIZE_MB` | `10` | Skip files larger than this |
| `MAX_MEMORY_MB` | `100` | Memory limit for indexing batch |

Override via environment variables:
```bash
PROJECTMIND_MAX_FILE_SIZE_MB=5
PROJECTMIND_MAX_MEMORY_MB=200
```

Custom ignore patterns: create `.ai/.indexignore` (same syntax as `.gitignore`).

---

## Project Structure

```
mcp_server.py           ← all MCP tool definitions
config.py               ← configuration
vector_store_manager.py ← ChromaDB wrapper + hybrid search
bm25_index.py           ← BM25 keyword index + RRF fusion
codebase_indexer.py     ← file scanning & AST-aware chunking
ast_splitter.py         ← tree-sitter parser (9 languages)
code_intelligence.py    ← import graph, complexity analysis, cached graph
memory_manager.py       ← persistent memory read/write
incremental_indexing.py ← change tracking
context.py              ← dependency injection
run_index.py            ← helper script for manual re-indexing
```

---

## Contributing

Issues and PRs are welcome. This is an open project — built in the open, improved in the open.

```bash
pip install -e ".[dev]"
pytest tests/
ruff check .
```

---

## License

MIT

---

*Built with AI assistance — was used throughout development for coding, debugging, refactoring, and documentation.*

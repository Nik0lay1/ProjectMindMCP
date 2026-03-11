import config
from context import get_context
from mcp_server import get_ignored_dirs, load_index_ignore_patterns, startup_check

startup_check()
ctx = get_context()
print("Initializing vector store...")
if ctx.vector_store.get_collection() is None:
    print("ERROR: Failed to initialize vector store")
else:
    print("Vector store ready, indexing with AST-aware chunking...")
    result = ctx.indexer.index_all(
        config.PROJECT_ROOT, get_ignored_dirs(), load_index_ignore_patterns(), force=True
    )
    print(result)

    print("\nTest search: 'vector store initialization'")
    results = ctx.vector_store.query(["vector store initialization"], n_results=3)
    if results and results.get("metadatas"):
        for meta in results["metadatas"][0]:
            print(
                f"  [{meta.get('symbol_type','?')}] {meta.get('symbol_name','?')} "
                f"in {meta.get('source','?').split('/')[-1].split(chr(92))[-1]} "
                f"(lines {meta.get('line_start',0)}-{meta.get('line_end',0)})"
            )

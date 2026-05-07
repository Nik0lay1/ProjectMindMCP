import importlib

for m in ["manifest", "maintenance", "query_router", "vector_store_manager", "mcp_server"]:
    mod = importlib.import_module(m)
    print(f"OK {m}")

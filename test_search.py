import os
import sys
sys.path.append(os.getcwd())

from mcp_server import search_codebase, get_index_stats

print("Testing search functionality...")

stats = get_index_stats()
print(f"Index stats: {stats}")

results = search_codebase("startup check")
print(f"\nSearch Results:\n{results}")

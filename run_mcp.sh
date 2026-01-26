#!/bin/bash
# Wrapper script for running ProjectMind MCP server
# Ensures proper environment and error handling for VS Code/Zencoder

set -e

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to project directory
cd "$SCRIPT_DIR"

# Activate virtual environment and run server
exec "$SCRIPT_DIR/.venv/bin/python" "$SCRIPT_DIR/mcp_server.py" "$@"

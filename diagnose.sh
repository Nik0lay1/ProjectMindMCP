#!/bin/bash
# MCP Server Diagnostic Script for VS Code/Zencoder

echo "================================================"
echo "ProjectMind MCP Server Diagnostics"
echo "================================================"
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "1. Checking Python executable..."
if [ -f ".venv/bin/python" ]; then
    echo "✅ venv Python found"
    .venv/bin/python --version
else
    echo "❌ venv Python not found"
    exit 1
fi
echo ""

echo "2. Checking MCP installation..."
if .venv/bin/python -c "import mcp.server.fastmcp" 2>/dev/null; then
    echo "✅ MCP installed"
    .venv/bin/python -m pip show mcp | grep Version
else
    echo "❌ MCP not installed"
    exit 1
fi
echo ""

echo "3. Checking dependencies..."
for pkg in chromadb sentence-transformers langchain-text-splitters GitPython; do
    if .venv/bin/python -c "import ${pkg//-/_}" 2>/dev/null; then
        echo "✅ $pkg installed"
    else
        echo "❌ $pkg not installed"
    fi
done
echo ""

echo "4. Testing server import..."
if .venv/bin/python -c "import sys; sys.path.insert(0, '.'); import mcp_server" 2>&1 | grep -q "Import OK\|ProjectMind"; then
    echo "✅ Server can be imported"
else
    echo "❌ Server import failed"
    .venv/bin/python -c "import sys; sys.path.insert(0, '.'); import mcp_server" 2>&1
fi
echo ""

echo "5. Testing stdio communication..."
if .venv/bin/python test_stdio.py 2>&1 | grep -q "Server responded successfully"; then
    echo "✅ Stdio communication works"
else
    echo "❌ Stdio communication failed"
    echo "Running full test..."
    .venv/bin/python test_stdio.py
fi
echo ""

echo "================================================"
echo "Configuration for Zencoder:"
echo "================================================"
echo ""
echo "Option 1 (Wrapper Script):"
echo '{'
echo '  "mcpServers": {'
echo '    "ProjectMind": {'
echo "      \"command\": \"$SCRIPT_DIR/run_mcp.sh\","
echo '      "args": []'
echo '    }'
echo '  }'
echo '}'
echo ""

echo "Option 2 (Direct Python with -u):"
echo '{'
echo '  "mcpServers": {'
echo '    "ProjectMind": {'
echo "      \"command\": \"$SCRIPT_DIR/.venv/bin/python\","
echo '      "args": ['
echo '        "-u",'
echo "        \"$SCRIPT_DIR/mcp_server.py\""
echo '      ],'
echo "      \"cwd\": \"$SCRIPT_DIR\""
echo '    }'
echo '  }'
echo '}'
echo ""

echo "================================================"
echo "Diagnostics complete!"
echo "================================================"

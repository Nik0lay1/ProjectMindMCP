#!/usr/bin/env python3
"""Test MCP server stdio communication"""

import json
import subprocess
import sys
from pathlib import Path


def test_mcp_server() -> None:
    """Test basic MCP server communication"""

    # Determine python executable path based on platform
    if sys.platform == "win32":
        python_path = Path(".venv") / "Scripts" / "python.exe"
    else:
        python_path = Path(".venv") / "bin" / "python"

    # Start server
    process = subprocess.Popen(
        [str(python_path), "mcp_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=0,
    )

    try:
        # Send initialize request
        initialize_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "test-client", "version": "1.0.0"},
            },
        }

        print("Sending initialize request...")
        request_str = json.dumps(initialize_request) + "\n"
        assert process.stdin is not None
        process.stdin.write(request_str)
        process.stdin.flush()

        # Read response
        print("Waiting for response...")
        assert process.stdout is not None
        response_line = process.stdout.readline()
        print(f"Response: {response_line}")

        if response_line:
            response = json.loads(response_line)
            print(f"Parsed response: {json.dumps(response, indent=2)}")

            if "result" in response:
                print("\n✅ Server responded successfully!")
                print(f"Server capabilities: {response['result'].get('capabilities', {})}")
                assert True
            elif "error" in response:
                print(f"\n❌ Server returned error: {response['error']}")
                raise AssertionError(f"Server returned error: {response['error']}")
        else:
            print("\n❌ No response from server")
            assert process.stderr is not None
            stderr = process.stderr.read()
            if stderr:
                print(f"Server stderr: {stderr}")
            raise AssertionError("No response from server")

    except json.JSONDecodeError as e:
        print(f"\n❌ JSON Error: {e}")
        assert process.stderr is not None
        stderr = process.stderr.read()
        if stderr:
            print(f"Server stderr: {stderr}")
        raise AssertionError(f"JSON decode error: {e}") from e
    finally:
        process.terminate()
        process.wait(timeout=1)


if __name__ == "__main__":
    try:
        test_mcp_server()
        sys.exit(0)
    except AssertionError:
        sys.exit(1)

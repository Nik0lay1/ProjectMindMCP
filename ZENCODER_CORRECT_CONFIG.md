# ✅ ПРАВИЛЬНА Конфігурація для Zencoder

## Проблема
Ти використовуєш `"file"`, але робочий приклад показує що треба `"command"`!

## Робочий приклад (Chakra UI):
```json
{
  "command": "npx",
  "args": ["-y", "@chakra-ui/react-mcp", "--stdio"]
}
```

## ✅ ПРАВИЛЬНА Конфігурація для ProjectMind

### Варіант 1: Wrapper Script
```json
{
  "zencoder.mcpServers": {
    "ProjectMind": {
      "command": "/Users/mykolariabokon/Documents/Projects/MCP/run_mcp.sh",
      "args": []
    }
  }
}
```

### Варіант 2: Прямий Python
```json
{
  "zencoder.mcpServers": {
    "ProjectMind": {
      "command": "/Users/mykolariabokon/Documents/Projects/MCP/.venv/bin/python",
      "args": [
        "-u",
        "/Users/mykolariabokon/Documents/Projects/MCP/mcp_server.py"
      ]
    }
  }
}
```

### Варіант 3: З env variables (Найнадійніший)
```json
{
  "zencoder.mcpServers": {
    "ProjectMind": {
      "command": "/Users/mykolariabokon/Documents/Projects/MCP/.venv/bin/python",
      "args": ["-u", "mcp_server.py"],
      "env": {
        "PYTHONUNBUFFERED": "1"
      },
      "cwd": "/Users/mykolariabokon/Documents/Projects/MCP"
    }
  }
}
```

## Повна Структура settings.json

```json
{
  "zencoder.mcpServers": {
    "chakra-ui": {
      "command": "npx",
      "args": ["-y", "@chakra-ui/react-mcp", "--stdio"]
    },
    "ProjectMind": {
      "command": "/Users/mykolariabokon/Documents/Projects/MCP/run_mcp.sh",
      "args": []
    }
  }
}
```

---

**Ключ: використовуй `"command"`, а не `"file"`!**

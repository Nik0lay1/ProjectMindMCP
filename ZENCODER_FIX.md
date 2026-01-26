# 🎯 ЗНАЙШЛИ ПРОБЛЕМУ!

## Помилка
```
The "file" argument must be of type string. Received undefined.
```

## Проблема
Zencoder очікує `"file"` замість `"command"`!

## ✅ ПРАВИЛЬНА Конфігурація для Zencoder

```json
{
  "zencoder.mcpServers": {
    "ProjectMind": {
      "file": "/Users/mykolariabokon/Documents/Projects/MCP/run_mcp.sh"
    }
  }
}
```

## Альтернативні Варіанти

### Варіант 1: Wrapper (Найкращий)
```json
{
  "zencoder.mcpServers": {
    "ProjectMind": {
      "file": "/Users/mykolariabokon/Documents/Projects/MCP/run_mcp.sh"
    }
  }
}
```

### Варіант 2: Прямий Python
```json
{
  "zencoder.mcpServers": {
    "ProjectMind": {
      "file": "/Users/mykolariabokon/Documents/Projects/MCP/.venv/bin/python",
      "args": [
        "-u",
        "/Users/mykolariabokon/Documents/Projects/MCP/mcp_server.py"
      ]
    }
  }
}
```

### Варіант 3: З cwd
```json
{
  "zencoder.mcpServers": {
    "ProjectMind": {
      "file": "/Users/mykolariabokon/Documents/Projects/MCP/.venv/bin/python",
      "args": ["-u", "mcp_server.py"],
      "cwd": "/Users/mykolariabokon/Documents/Projects/MCP"
    }
  }
}
```

## 🔑 Ключова Різниця

| Клієнт | Ключ для executable |
|--------|---------------------|
| Claude Desktop | `"command"` |
| VS Code Zencoder | `"file"` |
| JetBrains | `"command"` |

---

**Спробуй Варіант 1 першим!**

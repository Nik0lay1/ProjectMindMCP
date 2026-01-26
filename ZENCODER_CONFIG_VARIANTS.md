# Zencoder Configuration Variants

Різні варіанти конфігурації для Zencoder в VS Code.

## 🎯 Правильний Шлях

**Отримай свій шлях:**
```bash
cd /Users/mykolariabokon/Documents/Projects/MCP
pwd
# Скопіюй результат
```

---

## Варіант 1: zencoder.mcpServers

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

---

## Варіант 2: mcp.servers

```json
{
  "mcp.servers": {
    "ProjectMind": {
      "command": "/Users/mykolariabokon/Documents/Projects/MCP/run_mcp.sh",
      "args": []
    }
  }
}
```

---

## Варіант 3: Прямий Python з -u

```json
{
  "zencoder.mcpServers": {
    "ProjectMind": {
      "command": "/Users/mykolariabokon/Documents/Projects/MCP/.venv/bin/python",
      "args": [
        "-u",
        "/Users/mykolariabokon/Documents/Projects/MCP/mcp_server.py"
      ],
      "cwd": "/Users/mykolariabokon/Documents/Projects/MCP"
    }
  }
}
```

---

## Варіант 4: З явним env

```json
{
  "zencoder.mcpServers": {
    "ProjectMind": {
      "command": "/Users/mykolariabokon/Documents/Projects/MCP/.venv/bin/python",
      "args": ["-u", "/Users/mykolariabokon/Documents/Projects/MCP/mcp_server.py"],
      "cwd": "/Users/mykolariabokon/Documents/Projects/MCP",
      "env": {
        "PYTHONUNBUFFERED": "1",
        "PYTHONPATH": "/Users/mykolariabokon/Documents/Projects/MCP"
      }
    }
  }
}
```

---

## Варіант 5: Через uv (якщо є uv)

```json
{
  "zencoder.mcpServers": {
    "ProjectMind": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/mykolariabokon/Documents/Projects/MCP",
        "mcp_server.py"
      ]
    }
  }
}
```

---

## 🔍 Як Знайти Правильний Ключ?

### Метод 1: VS Code Settings UI
1. `Cmd+,` (Settings)
2. Пошук: "mcp"
3. Подивись які опції є

### Метод 2: Settings JSON
1. `Cmd+Shift+P` → "Preferences: Open Settings (JSON)"
2. Пошукай існуючі MCP конфігурації
3. Скопіюй формат

### Метод 3: Zencoder Docs
Перевір документацію Zencoder:
- GitHub репозиторій
- VS Code extension page
- Офіційна документація

---

## 🧪 Тестування

Після додавання конфігурації:

1. **Перезапусти VS Code** (обов'язково!)
2. **Перевір Output:**
   - `View` → `Output`
   - Вибери "Zencoder" або "MCP" з dropdown
3. **Спробуй команду:**
   ```
   @ProjectMind read_memory()
   ```

---

## 🐛 Якщо Не Працює

### Крок 1: Перевір логи
```
View → Output → Zencoder/MCP
```

### Крок 2: Перевір що сервер працює
```bash
cd /Users/mykolariabokon/Documents/Projects/MCP
./diagnose.sh
```

### Крок 3: Спробуй інший варіант конфігурації
Протестуй варіанти 1-5 по черзі.

### Крок 4: Перевір версію Zencoder
Можливо потрібне оновлення розширення.

---

## 📝 Приклад Логів (Успішний Запуск)

```
[Info] Starting MCP server: ProjectMind
[Info] Server ProjectMind initialized
[Info] Server ProjectMind capabilities: tools, resources, prompts
```

## 📝 Приклад Логів (Помилка)

```
[Error] Failed to start MCP server ProjectMind
[Error] Connection closed
```

Якщо бачиш помилку - спробуй інший варіант конфігурації.

---

**Створено:** 2025-12-16  
**Статус:** Сервер працює локально ✅  
**Проблема:** Конфігурація Zencoder ⚙️

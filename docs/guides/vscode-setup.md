# VS Code + Zencoder Setup Guide

Інструкції для підключення ProjectMind MCP до VS Code з Zencoder.ai.

## ✅ Статус Сервера

**ProjectMind MCP сервер працює!** Діагностика підтверджує:
- ✅ Python 3.10.19
- ✅ MCP 1.21.2 встановлено
- ✅ Stdio комунікація працює
- ✅ Сервер відповідає на JSON-RPC запити

**Проблема:** Конфігурація Zencoder.

## ❌ Типова Помилка

При використанні прямого шляху до Python:
```json
{
  "command": "/path/to/.venv/bin/python",
  "args": ["/path/to/mcp_server.py"]
}
```

Помилка: **"MCP error -32000: Connection closed"**

## 🔍 Діагностика (СПОЧАТКУ ЗАПУСТИ ЦЕ!)

Перед налаштуванням Zencoder, перевір що сервер працює:

```bash
cd /Users/mykolariabokon/Documents/Projects/MCP
./diagnose.sh
```

Це покаже конфігурацію для копіювання та перевірить чи все працює.

---

## ✅ Рішення 1: Wrapper Script (Рекомендовано)

### Крок 1: Отримати правильний шлях

Запусти діагностику (вище) або:
```bash
cd /Users/mykolariabokon/Documents/Projects/MCP
pwd
```

### Крок 2: Конфігурація в Zencoder Settings

**VS Code:** `Cmd+,` → пошук "zencoder" → "Edit in settings.json"

Додай MCP сервер:

```json
{
  "zencoder.mcpServers": {
    "ProjectMind": {
      "file": "/Users/mykolariabokon/Documents/Projects/MCP/run_mcp.sh"
    }
  }
}
```

**⚠️ ВАЖЛИВО:**
- Використовуй `"file"` замість `"command"` (це особливість Zencoder!)
- Заміни `/Users/mykolariabokon/Documents/Projects/MCP/` на твій повний шлях
- Перезапусти VS Code після зміни

---

## 💡 Рішення 2: Прямий Python (Альтернатива)

Якщо wrapper не працює:

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

**Ключові параметри:**
- `"file"` — шлях до Python (НЕ "command"!)
- `-u` — unbuffered output (критично для stdio)
- Повні абсолютні шляхи

---

## Рішення 3: Python з повним шляхом до модулів

Якщо все ще є проблеми:

```json
{
  "mcpServers": {
    "ProjectMind": {
      "command": "/Users/mykolariabokon/Documents/Projects/MCP/.venv/bin/python",
      "args": [
        "-u",
        "-m",
        "mcp_server"
      ],
      "cwd": "/Users/mykolariabokon/Documents/Projects/MCP",
      "env": {
        "PYTHONPATH": "/Users/mykolariabokon/Documents/Projects/MCP",
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

---

## Діагностика

### Перевірка 1: Чи працює сервер локально?

```bash
cd /Users/mykolariabokon/Documents/Projects/MCP
.venv/bin/python mcp_server.py
```

Повинно запуститися без помилок (натисніть Ctrl+C для зупинки).

### Перевірка 2: Чи встановлені всі залежності?

```bash
cd /Users/mykolariabokon/Documents/Projects/MCP
.venv/bin/python -c "import mcp.server.fastmcp; print('MCP OK')"
.venv/bin/python -c "import chromadb; print('ChromaDB OK')"
.venv/bin/python -c "import sentence_transformers; print('Transformers OK')"
```

Всі команди повинні вивести "...OK".

### Перевірка 3: Логи

Перевірте логи VS Code/Zencoder:
- VS Code: `View` → `Output` → вибрати "Zencoder" або "MCP"
- Шукайте повідомлення про помилки

---

## Відмінності VS Code vs JetBrains

### JetBrains
- Більш толерантний до конфігурацій
- Автоматично встановлює `cwd`
- Буферизація менш критична

### VS Code/Zencoder
- Строгіші вимоги до stdio
- Потрібен `-u` (unbuffered)
- Може вимагати явний `cwd`
- Чутливий до шляхів та env variables

---

## Загальні Помилки

### "Connection closed"
**Причина:** Сервер завершився раніше ніж встановив з'єднання  
**Рішення:**
- Використати wrapper script
- Додати `-u` flag
- Встановити `cwd`

### "Module not found"
**Причина:** Python не знаходить залежності  
**Рішення:**
- Встановити `PYTHONPATH` в env
- Використати `cwd`
- Перевірити віртуальне середовище

### "Permission denied"
**Причина:** Wrapper script не executable  
**Рішення:**
```bash
chmod +x /Users/mykolariabokon/Documents/Projects/MCP/run_mcp.sh
```

---

## Тестування Конфігурації

Після налаштування:

1. Перезапустіть VS Code/Zencoder
2. Відкрийте будь-який проект
3. У Zencoder chat спробуйте:
   ```
   @ProjectMind read_memory()
   ```

Якщо все працює, ви побачите відповідь з вмістом memory файлу.

---

## Підтримка

Якщо проблеми залишаються:

1. Перевірте версію Python: `python --version` (повинна бути 3.10+)
2. Переконайтеся що всі залежності встановлені: `pip list`
3. Перевірте логи VS Code Developer Tools: `Help` → `Toggle Developer Tools` → Console

---

**Створено:** 2025-12-16  
**Для:** VS Code + Zencoder.ai  
**Статус:** Tested ✅

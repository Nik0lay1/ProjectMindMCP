# Advanced Usage Guide

Power features and advanced workflows for ProjectMind.

## Incremental Indexing Deep Dive

### How It Works

Incremental indexing tracks file modification times in `.ai/index_metadata.json`:

```json
{
  "src/main.py": {
    "mtime": 1702742400.123,
    "indexed_at": "2025-12-16T09:00:00"
  }
}
```

**Process:**
1. Compare current file `mtime` with stored `mtime`
2. Index only changed files
3. Remove deleted files from index
4. Update metadata

**Performance:**
- Full index: ~5-10 seconds for 100 files
- Incremental: ~0.5 seconds for 5 changed files
- **Speedup:** 10-100x

### Best Practices

**When to use full indexing:**
```python
# New project
index_codebase()

# After major refactor
index_codebase(force=True)

# After switching branches with many changes
index_codebase(force=True)
```

**When to use incremental:**
```python
# Daily development
index_changed_files()

# After commits
auto_update_memory_from_commits()
index_changed_files()

# CI/CD pipeline
index_changed_files()
```

---

## Advanced Search Techniques

### Precision Search

**Find authentication code, Python only, high relevance:**
```python
search_codebase_advanced(
    query="JWT token validation",
    file_types=[".py"],
    exclude_dirs=["tests/", "migrations/"],
    min_relevance=0.6,
    n_results=3
)
```

### Multi-Stage Search

**1. Broad search:**
```python
results = search_codebase("database connection")
```

**2. Refine by file type:**
```python
results = search_codebase_advanced(
    "database connection",
    file_types=[".py"],
    min_relevance=0.5
)
```

**3. Exclude specific areas:**
```python
results = search_codebase_advanced(
    "database connection",
    file_types=[".py"],
    exclude_dirs=["tests/", "examples/"],
    min_relevance=0.7
)
```

### Query Optimization

✅ **Good queries:**
- "OAuth2 authentication flow"
- "error handling in API requests"
- "user registration validation"

❌ **Poor queries:**
- "function" (too generic)
- "a" (single character)
- "code that does stuff" (vague)

---

## Memory Versioning Workflows

### Pre-Refactor Workflow

```python
# 1. Save current state
save_memory_version("Before authentication refactor")

# 2. Update memory during refactor
update_memory("""
Refactoring authentication:
- Moving from sessions to JWT
- Adding refresh tokens
- Implementing OAuth2
""", section="In Progress")

# 3. If something goes wrong
restore_memory_version("20251216_090000")

# 4. After successful refactor
save_memory_version("After authentication refactor - JWT implemented")
```

### Sprint/Milestone Workflow

```python
# End of sprint 1
save_memory_version("Sprint 1 complete - User auth finished")

# End of sprint 2
save_memory_version("Sprint 2 complete - Payment integration")

# Review history
list_memory_versions()

# Compare with previous sprint
restore_memory_version("20251201_170000")  # Sprint 1
current = read_memory()
```

### Automated Backups

Create a pre-commit hook:
```bash
#!/bin/bash
# .git/hooks/pre-commit

# Auto-save memory before each commit
python -c "
from mcp_server import save_memory_version
import subprocess

commit_msg = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode().strip()[:50]
save_memory_version(f'Auto: {commit_msg}')
"
```

---

## Code Quality Workflows

### Weekly Quality Check

```python
# 1. Complexity analysis
complexity = analyze_code_complexity(".")
# Focus on functions with complexity > 15

# 2. Quality audit
quality = analyze_code_quality(".", max_files=50)
# Track error and warning trends

# 3. Coverage check
coverage = get_test_coverage_info()
# Goal: >80% coverage

# 4. Document findings
update_memory(f"""
Weekly Quality Check - {date}
- High complexity: {count} functions
- Pylint score: {score}
- Coverage: {coverage}%
- Action items: [list]
""", section="Quality Metrics")
```

### CI/CD Integration

**GitHub Actions example:**
```yaml
- name: Code Quality Check
  run: |
    python -c "
    from mcp_server import analyze_code_complexity, analyze_code_quality
    
    complexity = analyze_code_complexity('.')
    if 'High complexity' in complexity:
        print('⚠️ High complexity detected')
    
    quality = analyze_code_quality('.', max_files=100)
    # Parse and fail if errors > threshold
    "
```

---

## Git Integration Strategies

### Auto-Memory Updates

**Daily standup automation:**
```python
# Summarize yesterday's work
auto_update_memory_from_commits(days=1, auto_summarize=True)

# Read updated memory
summary = read_memory()
```

**Weekly team sync:**
```python
# Get weekly summary
changes = get_recent_changes_summary(days=7)

# Auto-update memory
auto_update_memory_from_commits(days=7, auto_summarize=True)

# Save weekly snapshot
save_memory_version("Week of Dec 16 - Sprint 5")
```

### Selective Git Ingestion

**Ingest only important commits:**
```python
# Get last 100 commits
ingest_git_history(limit=100)

# Or use auto-summarize for recent work
auto_update_memory_from_commits(days=30, auto_summarize=True)
```

---

## Custom Ignore Patterns

### .indexignore Examples

**Python project:**
```
# Tests
tests/
test_*.py
*_test.py

# Generated
*.pyc
__pycache__/
.pytest_cache/

# Docs
docs/
*.md

# Migrations
migrations/
alembic/

# Data
*.csv
*.json
*.sql
```

**JavaScript/TypeScript project:**
```
# Node
node_modules/
*.min.js

# Tests
**/*.test.ts
**/*.spec.ts
__tests__/

# Build
dist/
build/
*.map

# Docs
docs/
*.md
```

**Multi-language:**
```
# Python
venv/
*.pyc

# JavaScript
node_modules/
dist/

# General
tests/
docs/
*.md
*.log
*.tmp
```

---

## Performance Optimization

### Large Codebases (>1000 files)

**1. Increase file size limit:**
```bash
export PROJECTMIND_MAX_FILE_SIZE_MB=50
```

**2. Aggressive .indexignore:**
```
tests/
docs/
examples/
*.md
*.txt
*.log
```

**3. Use incremental indexing:**
```python
# Never do full re-index
index_changed_files()  # Always
```

**4. Increase batch size in config.py:**
```python
BATCH_SIZE = 500  # Default: 100
```

### Memory Usage

**Monitor index size:**
```python
stats = get_index_stats()
# If too large, review .indexignore
```

**Optimize memory file:**
```python
# Keep memory focused, under 10KB
# Use sections to organize
# Archive old sections
```

---

## Integration Examples

### VSCode Task

`.vscode/tasks.json`:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Index Changed Files",
      "type": "shell",
      "command": "python -c 'from mcp_server import index_changed_files; print(index_changed_files())'",
      "problemMatcher": []
    }
  ]
}
```

### Pre-Commit Hook

`.git/hooks/pre-commit`:
```bash
#!/bin/bash
# Auto-index changed files before commit
python -c "from mcp_server import index_changed_files; index_changed_files()"
```

### Makefile

```makefile
.PHONY: index quality memory

index:
	python -c "from mcp_server import index_changed_files; print(index_changed_files())"

quality:
	python -c "from mcp_server import analyze_code_complexity, analyze_code_quality; \
	print(analyze_code_complexity('.')); print(analyze_code_quality('.'))"

memory:
	python -c "from mcp_server import auto_update_memory_from_commits; \
	print(auto_update_memory_from_commits(days=7))"
```

---

## Troubleshooting

### Index Issues

**"Collection does not exist":**
```python
# Rebuild index
index_codebase(force=True)
```

**Outdated results:**
```python
# Re-index changed files
index_changed_files()
```

**Slow searches:**
```python
# Reduce n_results
search_codebase("query", n_results=3)

# Use filters
search_codebase_advanced("query", file_types=[".py"], min_relevance=0.5)
```

### Memory Issues

**Memory too large:**
```python
# Archive old sections
delete_memory_section("Old Sprint Notes")

# Save version first
save_memory_version("Before cleanup")
```

**Corrupted memory:**
```python
# Restore from version
list_memory_versions()
restore_memory_version("20251201_120000")
```

---

## Advanced Configuration

### Custom Embedding Model

Edit `config.py`:
```python
# Default: all-MiniLM-L6-v2 (fast, lightweight)
MODEL_NAME = "all-mpnet-base-v2"  # Better quality, slower

# Or use multilingual
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
```

### Custom Chunk Settings

```python
# Larger chunks = fewer chunks, less precise
CHUNK_SIZE = 2000
CHUNK_OVERLAP = 200

# Smaller chunks = more chunks, more precise
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
```

---

**Master ProjectMind workflows!** 💪

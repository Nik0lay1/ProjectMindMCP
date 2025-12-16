# ProjectMind: Local Context & Memory MCP Server

ProjectMind is a standalone MCP server that adds persistent memory and local vector search capabilities to your projects.

## Features

### Core Features
- **Self-Initialization**: Automatically sets up `.ai/` directory and `.gitignore`
- **Project Memory**: Persistent memory file (`.ai/memory.md`) readable via `project://memory`
- **Context Management**: Tools to update, clear, and delete memory sections
- **Git Integration**: Ingest git commit history into project memory to track development flow
- **Local RAG**: Index your codebase and search it using local embeddings

### Advanced Features
- **Smart Indexing**: 
  - **🆕 Incremental indexing** - Only re-index changed files (10-100x faster)
  - Filters binary and non-text files automatically
  - Configurable file size limits (default 10MB)
  - Custom ignore patterns via `.ai/.indexignore`
  - Supports 50+ programming languages and text formats
- **🆕 Advanced Search Filters**:
  - Filter by file types
  - Exclude directories
  - Minimum relevance threshold
  - Relevance scores in results
- **🆕 Automatic Memory Updates**:
  - Auto-summarize recent commits
  - Scheduled memory updates
  - Smart grouping by contributors
- **🆕 Code Quality & Metrics**:
  - Cyclomatic complexity analysis
  - Pylint quality checks
  - Test coverage tracking
  - Technical debt detection
- **🆕 Memory Versioning**:
  - Git-like versioning for memory
  - Timestamped snapshots
  - Easy rollback and restore
  - Version history tracking
- **Input Validation**: All tools have parameter validation and error handling
- **Memory Management**: Clear memory, delete specific sections, maintain templates
- **Index Statistics**: Track the number of indexed chunks
- **Type Safety**: Full type hints throughout the codebase
- **Environment Configuration**: Customize via environment variables

## Installation

### Prerequisites
- Python 3.10+
- `uv` (recommended) or `pip`

### Using `uv` (Recommended)

1. Clone or copy the server files to your project or a central location
2. Run the server directly:

```bash
uv run mcp_server.py
```

### Using `pip`

1. Install dependencies:

```bash
pip install -e .
# or for development
pip install -e ".[dev]"
```

2. Run the server:

```bash
python mcp_server.py
```

## IDE Configuration

To use ProjectMind with your IDE (e.g., Cursor, VS Code), add it to your MCP config.

**Command:** `uv`  
**Args:** `run`, `/absolute/path/to/mcp_server.py`

Or if using python directly:  
**Command:** `/path/to/python`  
**Args:** `/absolute/path/to/mcp_server.py`

## Available Tools

### Memory Management

#### `read_memory()`
Returns the current state of the project memory.

#### `update_memory(content: str, section: str = "Recent Decisions")`
Appends information to the project memory file under specified section.

#### `clear_memory(keep_template: bool = True)`
Clears the memory file. If `keep_template=True`, preserves the basic structure.

#### `delete_memory_section(section_name: str)`
Deletes a specific section from the memory file.

### Codebase Indexing & Search

#### `index_codebase(force: bool = False)`
Indexes the codebase for vector search.
- `force`: If true, clears existing index and rebuilds it
- Respects `.ai/.indexignore` patterns
- Automatically filters binary files and large files

#### `search_codebase(query: str, n_results: int = 5)`
Searches the codebase using vector similarity.
- `query`: Search query (required, non-empty)
- `n_results`: Number of results (1-50, default 5)

#### `get_index_stats()`
Returns statistics about the current vector store (number of chunks).

#### `index_changed_files()` 🆕
**Incremental indexing** - only indexes files that changed since last index.
- 10-100x faster for large codebases
- Tracks file modification times
- Automatically removes deleted files from index

**Use case:** Daily re-indexing, continuous development workflow.

#### `search_codebase_advanced(query, n_results=5, file_types=None, exclude_dirs=None, min_relevance=0.0)` 🆕
Advanced search with filters:
- `file_types`: List of extensions (e.g., `[".py", ".js"]`)
- `exclude_dirs`: Directories to skip (e.g., `["tests/", "docs/"]`)
- `min_relevance`: Minimum relevance score (0-1)

**Use case:** Precise search in specific parts of codebase.

```python
# Search only in Python files, exclude tests
search_codebase_advanced(
    "authentication",
    file_types=[".py"],
    exclude_dirs=["tests/"],
    min_relevance=0.5
)
```

### Project Analysis & Intelligence

#### `generate_project_summary()`
Generates comprehensive project summary including:
- Current memory state
- Recent git activity (last 5 commits)
- Codebase statistics
- Index stats

**Use case:** Quick project overview for onboarding or context refresh.

#### `extract_tech_stack()`
Automatically extracts technology stack from:
- `pyproject.toml` / `requirements.txt` (Python)
- `package.json` (JavaScript/Node.js)
- `Cargo.toml` (Rust)
- `go.mod` (Go)

**Use case:** Understand project dependencies without reading config files.

#### `analyze_project_structure()`
Analyzes and reports:
- Main directories by size
- File type distribution
- Configuration files present

**Use case:** Understand project organization and architecture.

#### `get_recent_changes_summary(days: int = 7)`
Provides summary of recent development activity:
- Total commits in period
- Contributors and their activity
- Recent commit messages
- `days`: Period to analyze (1-365, default 7)

**Use case:** Catch up after being away from project.

### Git Integration

#### `ingest_git_history(limit: int = 30)`
Reads git commit history and appends new commits to memory.
- `limit`: Number of recent commits to check (1-1000, default 30)

#### `auto_update_memory_from_commits(days=7, auto_summarize=True)` 🆕
Automatically updates memory with recent git activity:
- Analyzes commits from last N days
- Auto-summarizes if > 5 commits
- Groups by contributors
- Highlights key changes

**Use case:** Automated weekly memory updates.

### Code Quality & Metrics 🆕

#### `analyze_code_complexity(target_path=".")`
Analyzes code complexity using cyclomatic complexity:
- Identifies high-complexity functions (>10)
- Calculates average complexity
- Supports Python files

**Use case:** Find code that needs refactoring.

#### `analyze_code_quality(target_path=".", max_files=10)`
Runs pylint analysis on codebase:
- Counts errors, warnings, refactoring suggestions
- Convention issues
- Quality score

**Use case:** Code review, technical debt tracking.

#### `get_test_coverage_info()`
Reads test coverage reports:
- Parses `.coverage` and `htmlcov/` data
- Shows overall coverage percentage
- Provides links to detailed reports

**Use case:** Monitor test coverage trends.

### Memory Versioning 🆕

#### `save_memory_version(description="")`
Creates a versioned backup of memory:
- Timestamped snapshots
- Optional description
- Stored in `.ai/memory_history/`

**Use case:** Before major changes, milestone backups.

#### `list_memory_versions()`
Lists all saved memory versions with timestamps and descriptions.

#### `restore_memory_version(timestamp)`
Restores memory from a specific version:
- Auto-backs up current memory before restore
- Specify timestamp from list

**Use case:** Rollback after mistakes, recover old context.

```python
# Save before major refactoring
save_memory_version("Before microservices migration")

# List versions
list_memory_versions()

# Restore if needed
restore_memory_version("20241216_143022")
```

## Quick Start Examples

### New to the project?
```python
# Get instant overview
generate_project_summary()

# Understand tech stack
extract_tech_stack()

# See project structure
analyze_project_structure()
```

### Coming back after a break?
```python
# What happened in last 2 weeks?
get_recent_changes_summary(days=14)

# Re-index to catch new code
index_codebase()

# Refresh memory with recent commits
ingest_git_history(limit=50)
```

### Daily workflow
```python
# Morning: catch up
get_recent_changes_summary(days=1)

# Find implementation: "How do we handle authentication?"
search_codebase("authentication login", n_results=10)

# Document decision
update_memory("Switched to JWT tokens for better scalability", 
              section="Architecture Decisions")
```

## Configuration

### Environment Variables

- `PROJECTMIND_MAX_FILE_SIZE_MB`: Maximum file size to index in MB (default: 10)

### Custom Ignore Patterns

Create `.ai/.indexignore` to exclude specific files from indexing:

```
# Example .indexignore
test_data/
*.log
legacy/
```

### Code Configuration

Edit `config.py` to customize:
- Chunk size and overlap for text splitting
- Ignored directories
- File type extensions
- Batch size for indexing

## Development

### Running Tests

```bash
# Run all tests
python test_mcp_tools.py

# Run search test
python test_search.py
```

### Pre-commit Hooks

Install pre-commit hooks for code quality:

```bash
pip install pre-commit
pre-commit install
```

This will run:
- Black (code formatting)
- Ruff (linting)
- MyPy (type checking)
- YAML/JSON/TOML validators

### Code Quality Tools

```bash
# Format code
black .

# Lint code
ruff check . --fix

# Type check
mypy mcp_server.py config.py --ignore-missing-imports
```

## Resources

### `project://memory`
Reads the project memory file directly as a resource.

## Architecture

### Components

- **mcp_server.py**: Main server implementation with all MCP tools
- **config.py**: Centralized configuration management
- **pyproject.toml**: Modern Python project configuration
- **.pre-commit-config.yaml**: Pre-commit hooks for code quality
- **.github/workflows/ci.yml**: CI/CD pipeline configuration

### Technology Stack

- **MCP Server**: FastMCP
- **Vector Store**: ChromaDB (persistent)
- **Embeddings**: sentence-transformers (all-MiniLM-L6-v2)
- **Text Splitting**: LangChain RecursiveCharacterTextSplitter
- **Git Integration**: GitPython

## Troubleshooting

### Vector store not initialized
The vector store is lazy-loaded on first use. Run `index_codebase()` first.

### Large files being skipped
Files larger than 10MB are skipped by default. Set `PROJECTMIND_MAX_FILE_SIZE_MB` to increase the limit.

### Git history not showing
Ensure you're in a git repository. The tool searches parent directories automatically.

## Contributing

1. Fork the repository
2. Install development dependencies: `pip install -e ".[dev]"`
3. Install pre-commit hooks: `pre-commit install`
4. Make your changes
5. Run tests: `python test_mcp_tools.py`
6. Submit a pull request

## License

MIT License - feel free to use and modify as needed.

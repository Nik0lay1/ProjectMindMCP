# Changelog

## [0.3.0] - 2025-12-16 🚀 MAJOR UPDATE

### 🎉 5 Major New Features

#### 1️⃣ Incremental Indexing
- **`index_changed_files()`** - Only re-indexes modified files
- 10-100x faster for large codebases
- Automatic file modification tracking
- Smart deletion of removed files
- Metadata storage in `.ai/index_metadata.json`

#### 2️⃣ Advanced Search Filters
- **`search_codebase_advanced()`** with powerful filters:
  - Filter by file types (`.py`, `.js`, etc.)
  - Exclude specific directories
  - Minimum relevance threshold (0-1)
  - Relevance scores in search results
- Precise search in specific parts of codebase

#### 3️⃣ Automatic Memory Updates
- **`auto_update_memory_from_commits()`** - Smart git integration
- Auto-summarization of commits (when > 5)
- Groups changes by contributors
- Highlights key changes
- Configurable time period (1-90 days)

#### 4️⃣ Code Quality & Metrics
- **`analyze_code_complexity()`** - Cyclomatic complexity analysis
  - Identifies high-complexity functions (>10)
  - Average complexity calculation
  - Python support
- **`analyze_code_quality()`** - Pylint integration
  - Errors, warnings, refactoring suggestions
  - Convention issues tracking
  - Quality scoring
- **`get_test_coverage_info()`** - Coverage tracking
  - Parses `.coverage` and `htmlcov/`
  - Overall coverage percentage
  - Links to detailed reports

#### 5️⃣ Memory Versioning
- **`save_memory_version()`** - Create memory snapshots
- **`list_memory_versions()`** - View version history
- **`restore_memory_version()`** - Rollback to previous state
- Git-like versioning for memory.md
- Auto-backup before restore
- Stored in `.ai/memory_history/`

### 📦 New Dependencies
- `radon>=6.0.0` - Code complexity analysis
- `pylint>=3.0.0` - Code quality checks

### 📝 New Files
- `incremental_indexing.py` - Metadata management for incremental indexing
- `.ai/index_metadata.json` - File modification tracking
- `.ai/memory_history/` - Memory version storage

### 🔧 Infrastructure Changes
- Added `INDEX_METADATA_FILE` to config
- Added `MEMORY_HISTORY_DIR` to config
- New imports: `json`, `shutil`, `timedelta`
- Extended type hints with `Dict`

### ✅ Testing
- Added 5 new test suites
- Total test functions: 11
- Coverage for all new features

### 📚 Documentation
- Comprehensive README updates
- New sections for all 5 features
- Code examples for advanced features
- Updated Quick Start guide

---

## [0.2.0] - 2025-12-16

### 🎉 Major Improvements

#### Infrastructure
- ✅ Migrated from `requirements.txt` to modern `pyproject.toml`
- ✅ Added comprehensive `.gitignore` with Python-specific patterns
- ✅ Removed duplicate `venv/` directory
- ✅ Created centralized `config.py` for all configuration settings
- ✅ Added GitHub Actions CI/CD pipeline
- ✅ Configured pre-commit hooks for code quality

#### Code Quality
- ✅ Added comprehensive type hints throughout the codebase
- ✅ Implemented input validation for all tool parameters
- ✅ Enhanced error handling with proper exception management
- ✅ Improved code organization and structure
- ✅ Added security checks (bandit) to CI pipeline

#### New Features

**Memory Management:**
- ✅ `clear_memory(keep_template: bool)` - Clear memory with optional template preservation
- ✅ `delete_memory_section(section_name: str)` - Delete specific memory sections
- ✅ `get_index_stats()` - Get vector store statistics

**Smart Indexing:**
- ✅ File type filtering (50+ programming languages and text formats)
- ✅ File size limits (configurable, default 10MB)
- ✅ Custom ignore patterns via `.ai/.indexignore`
- ✅ Binary file detection and exclusion
- ✅ Improved file scanning performance

**Validation & Safety:**
- ✅ Query validation (non-empty, reasonable limits)
- ✅ Result count validation (1-50 range)
- ✅ Git history limit validation (1-1000 range)
- ✅ Empty content detection

#### Testing
- ✅ Expanded test suite with 5 test categories
- ✅ Fixed lazy loading issue in `test_search.py`
- ✅ Added validation tests
- ✅ Added memory management tests
- ✅ Added git integration tests
- ✅ Better error reporting with tracebacks

#### Documentation
- ✅ Completely rewritten README with detailed API documentation
- ✅ Added configuration guide
- ✅ Added troubleshooting section
- ✅ Added development and contribution guidelines
- ✅ Documented all new features and tools

### 🐛 Bug Fixes
- Fixed `test_search.py` attempting to import `collection` directly (lazy loading issue)
- Fixed missing error handling in indexing operations
- Fixed potential issues with empty file handling
- Fixed hardcoded configuration values

### 🔧 Configuration
- Configurable maximum file size via `PROJECTMIND_MAX_FILE_SIZE_MB` environment variable
- Centralized chunk size and overlap configuration
- Customizable ignored directories and file extensions
- Flexible batch size for indexing operations

### 📦 Dependencies
Added development dependencies:
- `pytest` & `pytest-cov` for testing
- `black` for code formatting
- `ruff` for linting
- `mypy` for type checking
- `pre-commit` for git hooks

### 🏗️ Architecture Changes
- Separated configuration into `config.py`
- Improved function signatures with type hints
- Better separation of concerns
- More maintainable and scalable codebase

---

## [0.1.0] - Initial Release

### Features
- Basic MCP server implementation
- Project memory management
- Git history ingestion
- Local RAG with ChromaDB
- Vector search functionality
- Auto-initialization of `.ai/` directory

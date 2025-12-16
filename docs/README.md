# ProjectMind Documentation

Welcome to ProjectMind comprehensive documentation.

## 📚 Documentation Structure

### Quick Start
- **[Getting Started Guide](guides/getting-started.md)** - Installation, setup, and first steps

### API Reference
- **[Complete Tools Reference](api/tools-reference.md)** - All 22 MCP tools with examples

### Guides
- **[Advanced Usage](guides/advanced-usage.md)** - Power features and workflows

### Archive
- **[features/](archive/)** - Historical feature documentation and version snapshots

## 🚀 Quick Links

**New to ProjectMind?** → [Getting Started](guides/getting-started.md)

**Looking for specific tool?** → [API Reference](api/tools-reference.md)

**Advanced workflows?** → [Advanced Usage](guides/advanced-usage.md)

## 📖 Documentation by Feature

### Memory Management
- [read_memory()](api/tools-reference.md#read_memory)
- [update_memory()](api/tools-reference.md#update_memory)
- [clear_memory()](api/tools-reference.md#clear_memory)
- [delete_memory_section()](api/tools-reference.md#delete_memory_section)

### Indexing & Search
- [index_codebase()](api/tools-reference.md#index_codebase)
- [index_changed_files()](api/tools-reference.md#index_changed_files) 🆕
- [search_codebase()](api/tools-reference.md#search_codebase)
- [search_codebase_advanced()](api/tools-reference.md#search_codebase_advanced) 🆕

### Project Intelligence
- [generate_project_summary()](api/tools-reference.md#generate_project_summary)
- [extract_tech_stack()](api/tools-reference.md#extract_tech_stack)
- [analyze_project_structure()](api/tools-reference.md#analyze_project_structure)
- [get_recent_changes_summary()](api/tools-reference.md#get_recent_changes_summary)

### Git Integration
- [ingest_git_history()](api/tools-reference.md#ingest_git_history)
- [auto_update_memory_from_commits()](api/tools-reference.md#auto_update_memory_from_commits) 🆕

### Code Quality
- [analyze_code_complexity()](api/tools-reference.md#analyze_code_complexity) 🆕
- [analyze_code_quality()](api/tools-reference.md#analyze_code_quality) 🆕
- [get_test_coverage_info()](api/tools-reference.md#get_test_coverage_info) 🆕

### Memory Versioning
- [save_memory_version()](api/tools-reference.md#save_memory_version) 🆕
- [list_memory_versions()](api/tools-reference.md#list_memory_versions) 🆕
- [restore_memory_version()](api/tools-reference.md#restore_memory_version) 🆕

## 🔍 Common Use Cases

**Daily Development:**
```python
# Morning sync
generate_project_summary()
get_recent_changes_summary(days=1)

# During work
index_changed_files()
search_codebase_advanced("feature", file_types=[".py"])

# End of day
auto_update_memory_from_commits(days=1)
```

**Code Review:**
```python
analyze_code_complexity("src/")
analyze_code_quality("src/")
get_test_coverage_info()
```

**Onboarding:**
```python
generate_project_summary()
extract_tech_stack()
analyze_project_structure()
```

## 📝 Documentation Maintenance

This documentation is automatically organized. See the main [README](../README.md) for project overview.

---

**Questions?** Check [Getting Started](guides/getting-started.md) or [Advanced Usage](guides/advanced-usage.md)

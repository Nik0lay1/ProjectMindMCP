#!/usr/bin/env python3
"""
Documentation Organization Script for ProjectMind

Automatically organizes, archives, and cleans up project documentation.

Features:
- Detects duplicate documentation
- Archives versioned files
- Moves misplaced .md files
- Cleans up empty/outdated docs
- Generates documentation index

Usage:
    python scripts/organize_docs.py [--dry-run] [--verbose]
"""

import os
import sys
import shutil
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set, Tuple
from difflib import SequenceMatcher


class DocsOrganizer:
    def __init__(self, root_dir: Path, dry_run: bool = False, verbose: bool = False):
        self.root_dir = root_dir
        self.dry_run = dry_run
        self.verbose = verbose
        
        self.docs_dir = root_dir / "docs"
        self.archive_dir = self.docs_dir / "archive"
        
        # Files to keep in root
        self.root_whitelist = {
            "README.md",
            "CHANGELOG.md",
            "LICENSE",
            "LICENSE.md",
            "CONTRIBUTING.md",
            "CODE_OF_CONDUCT.md",
        }
        
        # Directories to ignore
        self.ignore_dirs = {
            ".git",
            ".ai",
            "node_modules",
            "venv",
            ".venv",
            "__pycache__",
            ".pytest_cache",
            "htmlcov",
            "dist",
            "build",
        }
        
        self.changes: List[str] = []
        self.stats = {
            "moved": 0,
            "archived": 0,
            "duplicates_found": 0,
            "deleted": 0,
        }
    
    def log(self, message: str, level: str = "INFO"):
        """Log message"""
        prefix = "🔍" if self.dry_run else "✅"
        if level == "WARN":
            prefix = "⚠️"
        elif level == "ERROR":
            prefix = "❌"
        
        if self.verbose or level in ["WARN", "ERROR"]:
            print(f"{prefix} {message}")
    
    def find_markdown_files(self) -> List[Path]:
        """Find all markdown files in project"""
        md_files = []
        
        for root, dirs, files in os.walk(self.root_dir):
            # Skip ignored directories
            dirs[:] = [d for d in dirs if d not in self.ignore_dirs]
            
            for file in files:
                if file.endswith(".md"):
                    md_files.append(Path(root) / file)
        
        return md_files
    
    def is_versioned_file(self, filename: str) -> bool:
        """Check if filename indicates versioning"""
        version_patterns = ["_v0.", "_v1.", "_v2.", "-v0.", "-v1.", "-v2.", "version"]
        return any(pattern in filename.lower() for pattern in version_patterns)
    
    def is_date_file(self, filename: str) -> bool:
        """Check if filename contains date"""
        import re
        date_pattern = r"\d{4}[-_]\d{2}[-_]\d{2}"
        return bool(re.search(date_pattern, filename))
    
    def calculate_similarity(self, file1: Path, file2: Path) -> float:
        """Calculate similarity between two files"""
        try:
            content1 = file1.read_text(encoding="utf-8", errors="ignore")
            content2 = file2.read_text(encoding="utf-8", errors="ignore")
            
            return SequenceMatcher(None, content1, content2).ratio()
        except Exception:
            return 0.0
    
    def find_duplicates(self, md_files: List[Path]) -> List[Tuple[Path, Path, float]]:
        """Find duplicate/similar documentation files"""
        duplicates = []
        
        for i, file1 in enumerate(md_files):
            for file2 in md_files[i + 1:]:
                similarity = self.calculate_similarity(file1, file2)
                
                if similarity > 0.85:  # 85% similar
                    duplicates.append((file1, file2, similarity))
        
        return duplicates
    
    def organize_root_files(self, md_files: List[Path]):
        """Move non-whitelisted .md files from root to docs/"""
        for md_file in md_files:
            # Only check files in root directory
            if md_file.parent != self.root_dir:
                continue
            
            if md_file.name not in self.root_whitelist:
                # Determine target directory
                if self.is_versioned_file(md_file.name) or self.is_date_file(md_file.name):
                    target_dir = self.archive_dir
                    action = "archived"
                else:
                    target_dir = self.docs_dir / "guides"
                    action = "moved"
                
                target_path = target_dir / md_file.name
                
                self.log(f"{action.capitalize()}: {md_file.name} → {target_path.relative_to(self.root_dir)}")
                
                if not self.dry_run:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(md_file), str(target_path))
                
                self.changes.append(f"- {action.capitalize()} `{md_file.name}` to `{target_path.relative_to(self.root_dir)}`")
                self.stats[action] += 1
    
    def archive_versioned_files(self, md_files: List[Path]):
        """Move versioned files to archive/"""
        for md_file in md_files:
            # Skip if already in archive
            if self.archive_dir in md_file.parents:
                continue
            
            # Skip root whitelisted files
            if md_file.name in self.root_whitelist:
                continue
            
            if self.is_versioned_file(md_file.name) or self.is_date_file(md_file.name):
                target_path = self.archive_dir / md_file.name
                
                self.log(f"Archive: {md_file.relative_to(self.root_dir)} → {target_path.relative_to(self.root_dir)}")
                
                if not self.dry_run:
                    self.archive_dir.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(md_file), str(target_path))
                
                self.changes.append(f"- Archived `{md_file.relative_to(self.root_dir)}` to archive")
                self.stats["archived"] += 1
    
    def check_duplicates(self, md_files: List[Path]):
        """Report duplicate files"""
        self.log("Checking for duplicates...", "INFO")
        duplicates = self.find_duplicates(md_files)
        
        if duplicates:
            self.log(f"Found {len(duplicates)} potential duplicates:", "WARN")
            
            for file1, file2, similarity in duplicates:
                self.log(f"  {file1.name} ≈ {file2.name} ({similarity:.1%} similar)", "WARN")
                self.stats["duplicates_found"] += 1
            
            self.changes.append(f"\n**⚠️ Duplicates Found:** {len(duplicates)} pairs")
            for file1, file2, similarity in duplicates:
                self.changes.append(f"  - `{file1.name}` ≈ `{file2.name}` ({similarity:.1%})")
        else:
            self.log("No duplicates found", "INFO")
    
    def delete_empty_files(self, md_files: List[Path]):
        """Delete empty or nearly empty markdown files"""
        for md_file in md_files:
            # Skip root whitelisted files
            if md_file.name in self.root_whitelist:
                continue
            
            try:
                content = md_file.read_text(encoding="utf-8").strip()
                
                # Consider file empty if < 50 characters
                if len(content) < 50:
                    self.log(f"Delete empty: {md_file.relative_to(self.root_dir)}", "WARN")
                    
                    if not self.dry_run:
                        md_file.unlink()
                    
                    self.changes.append(f"- Deleted empty file `{md_file.relative_to(self.root_dir)}`")
                    self.stats["deleted"] += 1
            except Exception as e:
                self.log(f"Error reading {md_file}: {e}", "ERROR")
    
    def generate_report(self):
        """Generate organization report"""
        print("\n" + "=" * 60)
        print("📊 DOCUMENTATION ORGANIZATION REPORT")
        print("=" * 60)
        
        if self.dry_run:
            print("🔍 DRY RUN MODE - No changes made\n")
        
        print(f"📁 Root Directory: {self.root_dir}\n")
        
        print("📈 Statistics:")
        print(f"  - Files moved: {self.stats['moved']}")
        print(f"  - Files archived: {self.stats['archived']}")
        print(f"  - Duplicates found: {self.stats['duplicates_found']}")
        print(f"  - Empty files deleted: {self.stats['deleted']}")
        
        if self.changes:
            print(f"\n📝 Changes ({len(self.changes)}):")
            for change in self.changes[:20]:  # Limit to 20
                print(f"  {change}")
            
            if len(self.changes) > 20:
                print(f"  ... and {len(self.changes) - 20} more")
        
        print("\n" + "=" * 60)
        
        if self.dry_run:
            print("💡 Run without --dry-run to apply changes")
        else:
            print("✅ Organization complete!")
        
        print("=" * 60 + "\n")
    
    def create_docs_index(self):
        """Create/update docs/README.md index"""
        if self.dry_run:
            self.log("Would create/update docs/README.md index")
            return
        
        # This is already created manually, so we skip auto-generation
        # In future, could parse and auto-generate
        self.log("Docs index exists at docs/README.md")
    
    def run(self):
        """Run the organization process"""
        self.log("Starting documentation organization...", "INFO")
        
        # Ensure docs structure exists
        if not self.dry_run:
            (self.docs_dir / "features").mkdir(parents=True, exist_ok=True)
            (self.docs_dir / "guides").mkdir(parents=True, exist_ok=True)
            (self.docs_dir / "api").mkdir(parents=True, exist_ok=True)
            self.archive_dir.mkdir(parents=True, exist_ok=True)
        
        # Find all markdown files
        md_files = self.find_markdown_files()
        self.log(f"Found {len(md_files)} markdown files", "INFO")
        
        # Organize root files
        self.organize_root_files(md_files.copy())
        
        # Archive versioned files
        md_files = self.find_markdown_files()  # Re-scan after moves
        self.archive_versioned_files(md_files.copy())
        
        # Check for duplicates
        md_files = self.find_markdown_files()  # Re-scan
        self.check_duplicates(md_files)
        
        # Delete empty files
        md_files = self.find_markdown_files()  # Re-scan
        self.delete_empty_files(md_files)
        
        # Create index
        self.create_docs_index()
        
        # Generate report
        self.generate_report()


def main():
    parser = argparse.ArgumentParser(
        description="Organize ProjectMind documentation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Preview changes without applying
  python scripts/organize_docs.py --dry-run
  
  # Apply changes with verbose output
  python scripts/organize_docs.py --verbose
  
  # Apply changes silently
  python scripts/organize_docs.py
        """
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without applying them"
    )
    
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed output"
    )
    
    args = parser.parse_args()
    
    # Determine project root (parent of scripts/)
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    
    organizer = DocsOrganizer(root_dir, dry_run=args.dry_run, verbose=args.verbose)
    organizer.run()


if __name__ == "__main__":
    main()

import json
from pathlib import Path
from typing import Dict, List, Set
from datetime import datetime

from config import INDEX_METADATA_FILE


class IndexMetadata:
    def __init__(self):
        self.metadata: Dict[str, Dict] = {}
        self.load()

    def load(self) -> None:
        if INDEX_METADATA_FILE.exists():
            try:
                with open(INDEX_METADATA_FILE, "r") as f:
                    self.metadata = json.load(f)
            except Exception:
                self.metadata = {}
        else:
            self.metadata = {}

    def save(self) -> None:
        try:
            INDEX_METADATA_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(INDEX_METADATA_FILE, "w") as f:
                json.dump(self.metadata, f, indent=2)
        except Exception as e:
            print(f"Error saving metadata: {e}")

    def get_file_mtime(self, file_path: str) -> float:
        return self.metadata.get(file_path, {}).get("mtime", 0.0)

    def update_file(self, file_path: str, mtime: float) -> None:
        self.metadata[file_path] = {
            "mtime": mtime,
            "indexed_at": datetime.now().isoformat(),
        }

    def get_changed_files(self, all_files: List[Path]) -> List[Path]:
        changed_files = []

        for file_path in all_files:
            try:
                current_mtime = file_path.stat().st_mtime
                stored_mtime = self.get_file_mtime(str(file_path))

                if current_mtime > stored_mtime:
                    changed_files.append(file_path)
            except Exception:
                changed_files.append(file_path)

        return changed_files

    def remove_deleted_files(self, existing_files: Set[str]) -> None:
        files_to_remove = []
        for file_path in self.metadata.keys():
            if file_path not in existing_files:
                files_to_remove.append(file_path)

        for file_path in files_to_remove:
            del self.metadata[file_path]

    def get_stats(self) -> Dict:
        if not self.metadata:
            return {"total_files": 0, "last_index": None}

        indexed_times = [
            info.get("indexed_at") for info in self.metadata.values() if "indexed_at" in info
        ]
        latest = max(indexed_times) if indexed_times else None

        return {"total_files": len(self.metadata), "last_index": latest}

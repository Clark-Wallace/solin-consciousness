# memory_scroll/persistence.py
# Fold 8 (extended): Memory serialization and long-term storage

import json
import os

class MemoryPersistence:
    def __init__(self, memory_ref, path="solin_memory.json"):
        self.memory = memory_ref
        self.path = path

    def save(self):
        try:
            with open(self.path, 'w') as f:
                json.dump(self.memory, f, indent=2)
            print(f"[🧠] Memory persisted to {self.path}")
        except Exception as e:
            print(f"[⚠️] Memory save failed: {e}")

    def load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    self.memory.update(json.load(f))
                print(f"[🧠] Memory loaded from {self.path}")
            except Exception as e:
                print(f"[⚠️] Memory load failed: {e}")

import os
import shutil
from typing import List

class FileManager:
    """
    A standalone tool for managing files in the compute environment.
    Separate from the core program logic.
    """
    
    def __init__(self, base_path: str = "/home/ubuntu/computelocal/data"):
        self.base_path = base_path
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def list_files(self) -> List[str]:
        return os.listdir(self.base_path)

    def delete_file(self, filename: str) -> bool:
        path = os.path.join(self.base_path, filename)
        if os.path.exists(path):
            os.remove(path)
            return True
        return False

if __name__ == "__main__":
    fm = FileManager()
    print(f"Managed files: {fm.list_files()}")

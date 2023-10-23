import os
import sys
from pathlib import Path


class Config:
    BASE_DIR = os.path.join(Path(__file__).parent)

    def apply_config(self):
        sys.path.insert(0, self.BASE_DIR)

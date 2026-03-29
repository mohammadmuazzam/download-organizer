import logging
from pathlib import Path

def get_all_files(path:str) -> list:
    dir = Path(path)
    contents = [f.name for f in dir.iterdir() if f.is_file()]
    return contents
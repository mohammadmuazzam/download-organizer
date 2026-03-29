import os, logging
import rename_rules
from pathlib import Path

logger = logging.getLogger(__name__)

def rename_all_files(folder_path:str = os.path.join(os.path.expanduser('~'), 'Downloads')):
    files = _get_all_files(folder_path)

    for file in files:
        old_path = os.path.join(folder_path, file)
        new_name = rename_rules.get_new_name(file)
        new_path = os.path.join(folder_path, new_name)

        if old_path != new_path:
            _rename_file(old_path, new_path)

def _rename_file(old_path: str, new_path: str):
    if os.path.exists(new_path):
        new_path = _resolve_duplicate_name(new_path)
        logging.info(f"Duplicate name. Renaming to '{new_path}'")

    try:
        os.rename(old_path, new_path)
        logging.info(f"Successfully renamed '{old_path}' to '{new_path}'")
        return True
    except PermissionError:
        logging.error(f"Error: Permission denied for '{old_path}'. Is the file open?")
    except FileNotFoundError:
        logging.error(f"Error: '{old_path}' was not found.")
    except OSError as e:
        logging.error(f"System Error: {e}")


def _resolve_duplicate_name(new_path: str) -> str:
    base, ext = os.path.splitext(new_path)
    counter = 1

    while os.path.exists(new_path):
        new_path = f"{base}_({counter}){ext}"
        counter += 1
    return new_path

def _get_all_files(path:str) -> list:
    logging.info(f"Renaming files in:{path}")
    dir = Path(path)
    contents = [f.name for f in dir.iterdir() if f.is_file()]
    return contents

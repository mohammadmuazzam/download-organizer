import hashlib, os, logging
import src.helper as helper
from src.rename import _resolve_duplicate_name

logger = logging.getLogger(__name__)
def detect_duplicates(path:str) -> None:
    files = helper.get_all_files(path)

    size_map = {}
    for file in files:
        file_path = os.path.join(path, file)
        size = os.path.getsize(file_path)
        if size in size_map:
            size_map[size].append(file_path)
        else:
            size_map[size] = [file_path]

    duplicates = _find_duplicates(size_map)
    logging.info(f"Found {len(duplicates)} sets of duplicates.")
    _handle_duplicates(duplicates)

def _get_file_hash(file_path:str, bytes_to_read:int = None) -> str:
    hasher = hashlib.sha256()

    with open(file_path, 'rb') as f:
        if bytes_to_read:
            chunk = f.read(bytes_to_read)
            hasher.update(chunk)
        else:
            while chunk := f.read(8192):
                hasher.update(chunk)
    return hasher.hexdigest()

def _find_duplicates(size_map:dict) -> list:
    files_with_same_size = _find_same_file_size(size_map)
    ##print(f"Phase 1 - Size check: {len(files_with_same_size)} potential duplicates found.")
    
    potential_duplicates = _find_same_partial_hash(files_with_same_size)
    ##print(f"potential_duplicates: {len(potential_duplicates)}")

    duplicates = _find_same_full_hash(potential_duplicates)

    return duplicates

def _find_same_file_size(size_map:dict) -> list:
    possible_duplicates = []
    for _, files in size_map.items():
        if len(files) > 1:
            possible_duplicates.extend(files)
    return possible_duplicates

# hash only the first 1KB of files with same size
def _find_same_partial_hash(files:list) -> dict:
    hash_map = {}
    for file in files:
        file_hash = _get_file_hash(file, bytes_to_read=1024)
        if file_hash in hash_map:
            hash_map[file_hash].append(file)
        else:
            hash_map[file_hash] = [file]
    
    potential_duplicates = {}
    for hash, files in hash_map.items():
        if len(files) > 1:
            potential_duplicates[hash] = files
    return potential_duplicates

def _find_same_full_hash(potential_duplicates:dict) -> dict:
    full_hash_map = {}
    for _, files in potential_duplicates.items():
        for file in files:
            full_hash = _get_file_hash(file)
            if full_hash in full_hash_map:
                full_hash_map[full_hash].append(file)
            else:
                full_hash_map[full_hash] = [file]

    # checking which full hashes have more than 1 file
    duplicates = {}
    for hash, files in full_hash_map.items():
        print(files)
        if len(files) > 1:
            files.sort(key=len)
            duplicates[hash] = files
    return duplicates

# move duplicates to a "Duplicates" folder
def _handle_duplicates(duplicates:dict) -> None:
    for _, files in duplicates.items():
        for file in files[1:]:
            duplicate_folder = os.path.join(os.path.dirname(file), "Duplicates")
            os.makedirs(duplicate_folder, exist_ok=True)
            new_path = os.path.join(duplicate_folder, os.path.basename(file))

            if os.path.exists(new_path):
                new_path = _resolve_duplicate_name(new_path)
                logging.info(f"Duplicate name in Duplicates folder. Renaming from '{file}' to '{new_path}'")

            try:
                os.rename(file, new_path)
                logging.info(f"Moved duplicate '{file}' to '{new_path}'")
            except Exception as e:
                logging.error(f"Error moving '{file}': {e}")
import os, random
from pathlib import Path

garbage_files = [
        "My   File   With   Spaces.txt",
        "UPPERCASE_NAME.PDF",
        "multiple...dots...in..name.png",
        "special!@#$%^chars.docx",
        "duplicate_test.txt",
        "duplicate_test.txt",
        ".hidden_system_file",
        "Folder_To_Ignore",
        "2nd Folder#ab"
    ]

random_files = [f"random_file_{i}.bin" for i in range(1, 1100)]

def _setup_test_folder(folder_name="test_folder"):
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    download_dir = Path(download_path)
    test_path = Path(folder_name)
    test_path = download_dir / test_path
    test_path.mkdir(exist_ok=True)

    random_data_multiplier = [m*1024 for m in range(1, 10240)]

    for name in random_files + garbage_files:
        file_path = test_path / name
        if "Folder" in name:
            file_path.mkdir(exist_ok=True)
        else:
            _create_garbage_files(file_path, random.choice(random_data_multiplier))
            
    print(f"Test environment ready in: '{test_path.absolute()}'")

def _create_garbage_files(file_path: Path, size_in_bytes: int) -> None:
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size_in_bytes))

if __name__ == "__main__":
    _setup_test_folder()
import os
from pathlib import Path

def setup_test_folder(folder_name="test_folder"):
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    download_dir = Path(download_path)
    test_path = Path(folder_name)
    test_path = download_dir / test_path
    test_path.mkdir(exist_ok=True)

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

    for name in garbage_files:
        file_path = test_path / name
        if "Folder" in name:
            file_path.mkdir(exist_ok=True)
        else:
            file_path.touch()
            
    print(f"Test environment ready in: '{test_path.absolute()}'")

if __name__ == "__main__":
    setup_test_folder()
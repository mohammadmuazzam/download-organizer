import os

def _get_all_files() -> list:
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    contents = os.listdir(download_path)
    return contents

def rename_all_files():
    files = _get_all_files()
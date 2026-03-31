# organizes files into folders based on their type

import src.helper as helper
import os, logging
from pathlib import Path
from enum import Enum

logger = logging.getLogger(__name__)




def organize_files_by_type(folder_path: str):
    files = helper.get_all_files(folder_path)
    logging.info(f"Organizing files in: '{folder_path}'")

    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_type = FileCategory.get_category(FileCategory, file)
            target_folder = os.path.join(folder_path, file_type)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            new_path = os.path.join(target_folder, file)
            try:
                os.rename(file_path, new_path)
                logging.info(f"Moved '{file}' to '{target_folder}'")
            except Exception as e:
                logging.error(f"Error moving '{file}': {e}")

# basic file type categorization based on file extension (not safe! but we don't care for now)  
class FileCategory(Enum):
    IMAGES = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    VIDEOS = ['.mp4', '.avi', '.mkv', '.mov', '.flv']
    DOCS = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.md']
    EXECUTABLES = ['.exe', '.msi', '.bat', '.sh']
    OTHERS = []

    def get_category(self, file:str) -> str:
        ext = Path(file).suffix.lower()
        for category in self:
            if ext in category.value:
                return category.name
        return self.OTHERS.name

#organize_files_by_type(r"C:\Users\LENOVO\Downloads\test_folder")
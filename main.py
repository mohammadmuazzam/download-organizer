import logging, os
import src.rename as rename, src.duplicate_detection as duplicate_detection, src.organize as organize

logger = logging.getLogger(__name__)
logging.basicConfig(
        filename="organizer.log", 
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

def main(path:str  = os.path.join(os.path.expanduser('~'), 'Downloads')):
    rename.rename_all_files(path)
    ##duplicate_detection.detect_duplicates(path)
    organize.organize_files_by_type(path)


if __name__ == "__main__":
    logging.info("STARTING PROCESS")
    path = r"C:\Users\LENOVO\Downloads\test_folder"
    main(path)
    logging.info("FINISHED PROCESS")

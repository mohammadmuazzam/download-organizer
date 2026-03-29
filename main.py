import logging, os
import src.rename as rename, src.duplicate_detection as duplicate_detection

logger = logging.getLogger(__name__)
logging.basicConfig(
        filename="organizer.log", 
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

def main(path:str  = os.path.join(os.path.expanduser('~'), 'Downloads')):
    duplicate_detection.detect_duplicates(path)

if __name__ == "__main__":
    logging.info("Starting process")
    path = r"C:\Users\LENOVO\Downloads\test_folder"
    main(path)
    logging.info("Finished process")

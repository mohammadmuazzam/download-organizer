import logging, rename

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        filename="organizer.log", 
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    path = r"C:\Users\LENOVO\Downloads\test_folder"
    rename.rename_all_files(path)

if __name__ == "__main__":
    logging.info("Starting process")
    main()
    logging.info("Finished process")

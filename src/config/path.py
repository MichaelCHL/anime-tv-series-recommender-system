from pathlib import Path
from utils.logger import get_logger

logger = get_logger(__name__)

ROOT_DIR = Path(__file__).resolve().parents[2]
ARTIFACTS_DIR = ROOT_DIR / "artifacts"
SRC_DIR = ROOT_DIR / "src"
RAW_DATA_DIR = ARTIFACTS_DIR / "raw"
PROCESSED_DATA_DIR = ARTIFACTS_DIR / "processed"
MODELS_DIR = ARTIFACTS_DIR / "models"
FEATURE_DIR = ARTIFACTS_DIR / "features"

def main():
    try: 
        logger.info("Start creating directories...")
        for path in [RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, FEATURE_DIR]:
            path.mkdir(parents=True, exist_ok=True)
        logger.info("Directories created successfully!")
    except Exception as e:
        logger.error("Failed to create directories!")
        raise Exception ("Failed to create directories!", e)

if __name__ == "__main__":
    main()


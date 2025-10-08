import os
import pandas as pd
import numpy as np
from utils.logger import get_logger
from utils.text_processing import *
from custom_exception import *

logger = get_logger(__name__)

class DataPreprocess:
    def __init__(self, path):
        self.path = path
        os.makedirs('artifacts/processed', exist_ok=True)
        self.output_path = 'artifacts/processed/output.csv'
        self.df = None

    def load_data(self):
        logger.info("Loading data...")

        try:
            self.df = pd.read_csv(self.path)    
            logger.info("Data loaded successfully!")
        except Exception as e:
            logger.error("Failed to load data")
            raise DataLoadingException("Fail to load data", e)

    def data_cleaning(self, cols: list):
        logger.info("Cleaning data...")

        try:
            for col in cols:
                new_col_name = col + '_cleaned'
                self.df[new_col_name] = self.df[col].apply(text_cleaning)
        
        except Exception as e:
            logger.error("Failed to clean data")
            raise DataCleaningException("Failed to clean data", e)


    def feature_preparation(self, year_col=None):
        logger.info("Starting feature preparation process...")
        try :
            # get the aired year
            if year_col:
                self.df['year'] = self.df[year_col].apply(find_year)
            # create text corpus column
            self.df['text_corpus'] = self.df['English_name_cleaned'] + self.df['Genres_cleaned'] + self.df['Synopsis_cleaned']
            self.df.to_csv(self.output_path)
            logger.info(f"Feature prepared successfully! Data is saved to {self.output_path}")

        except Exception as e:
            logger.error("Failed to complete feature preparation")
            raise FeaturePreparationException("Failed to complete feature preparation", e)
            
    def run(self):
        self.load_data()
        self.data_cleaning(['English_name', 'Genres', 'Synopsis'])
        self.feature_preparation('Aired')
        logger.info("Data preproccessing has successfully completed!")

if __name__ == "__main__":
    data_preprocessor = DataPreprocess('artifacts/raw/anime-dataset-2023.csv')
    data_preprocessor.run()


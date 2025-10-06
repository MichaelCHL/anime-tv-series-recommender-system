import nltk
import re
import os
import pandas as pd
import numpy as np
from utils.logger import logger
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from custom_exception import *

nltk.download('stopwrods')
nltk.download('punkt')

class DataPreprocess:
    def __init__(self, path):
        self.path = path
        os.makedirs('../artifacts/processed/', exist_ok=True)
        self.output = '../artifacts/processed/output.csv'
        self.df = None

    def load_data(self):
        logger.info("Loading data...")

        try:
            self.df = pd.read_csv(self.path)    
            logger.info("Data loaded successfully!")
        except Exception as e:
            logger.error("Failed to load data")
            raise DataLoadingException("Fail to load data", e)

    def data_cleaning(self, cols):
        logger.info("Cleaning data...")
        stop_words = set(stopwords.words('english'))

        try:
            for col in cols:
                new_col_name = col + '_cleaned'
            
                # get english stopwords and tokenize 
                tokens = word_tokenize(col.lower())
            
                # remove stopwords
                self.df[new_col_name] = [word for word in tokens if word not in stop_words]
        except Exception as e:
            logger.error("Failed to clean data")
            raise DataCleaningException("Failed to clean data", e)


    def feature_preparation    
        if year_col:
            self.df['year'] = self.df[year_col].apply(lambda x: re.findall(r"\b\d{4}\b", x)[0])

    def year_conversion(self, col):
        year = re.findall(r"\b\d{4}\b", col)
        
        return year[0] if year else None



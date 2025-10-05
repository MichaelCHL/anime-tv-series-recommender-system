import nltk
import re
import os
import pandas as pd
import numpy as np
from utils.logger import logger
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from custom_exception import DataLoadingException

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
        except DataLoadingException as e:
            logger.error("Fail to load data")
            raise DataLoadingException("Fail to load data", e)

    def stopword_remove(col):
        # get english stopwords and tokenize 
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(col.lower())
        
        # remove stopwords
        self.df[] filtered_tokens = [word for word in tokens if word not in stop_words]

        return filtered_tokens

    def year_conversion(self, date_str):
        year = re.findall(r"\b\d{4}\b", date_str)
        return year[0] if year else None



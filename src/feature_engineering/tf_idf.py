from utils.logger import get_logger
from custom_exception import *
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
import pandas as pd
import os
import joblib

logger = get_logger(__name__)

class vertorization:
    def __init__(self):
        self.output_path = '../artifacts/processed/'
        os.makedirs = os.makedirs(os.path.join(self.output_path, 'models'), exist_ok=True)
        self.data_path = os.path.join(self.output_path, 'processed')
        self.df = None

    def load_data(self):
        try:
            logger.info("Reading data...")
            self.df = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully!")

        except Exception as e:
            logger.error("Failed to load data")
            raise DataLoadingException("Failed to load data", e)
        
    def td_idf(self):
        try:
            logger.info("Start tf-idf vectorization...")
            corpus = self.df['text_courpus']
            vectorizer = TfidfVectorizer()
            X = vectorizer.fit_transform(corpus)
            
            return vectorizer

        except Exception as e:
            logger.error("Failed to convert to td-idf!")
            raise VectorizationException("Failed to vectorize corpus", e)

    
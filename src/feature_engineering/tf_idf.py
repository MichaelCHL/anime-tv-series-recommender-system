from utils.logger import get_logger
from custom_exception import *
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from scipy.sparse import save_npz
from config.path import PROCESSED_DATA_DIR, MODELS_DIR, FEATURE_DIR

import pandas as pd
import os
import joblib

logger = get_logger(__name__)

class Vectorization:
    def __init__(self):
        self.data_dir = PROCESSED_DATA_DIR / "output.csv"
        self.model_dir = MODELS_DIR
        self.feature_dir = FEATURE_DIR
        self.df = None

    def load_data(self):
        try:
            logger.info("Reading data...")
            self.df = pd.read_csv(self.data_dir)
            logger.info("Data loaded successfully!")

        except Exception as e:
            logger.error("Failed to load data")
            raise DataLoadingException("Failed to load data", e)
        
    def td_idf(self):
        try:
            logger.info("Start tf-idf vectorization...")
            corpus = self.df['text_corpus']
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform(corpus)
            
            model_file_dir = os.path.join(self.model_dir, 'tfidf_vectorizer.pkl')
            joblib.dump(vectorizer, model_file_dir)

            feature_file_dir = os.path.join(self.feature_dir, 'tfidf_matrix.npz')
            save_npz(feature_file_dir, tfidf_matrix)
            
            logger.info("tf-idf vectorization completed successfully!")


        except Exception as e:
            logger.error("Failed to convert to td-idf!")
            raise VectorizationException("Failed to vectorize corpus", e)

    def run(self):
        logger.info("Starting vectorization process...")
        self.load_data()
        self.td_idf()

if __name__ == '__main__':
    vectorizer = Vectorization()
    vectorizer.run()

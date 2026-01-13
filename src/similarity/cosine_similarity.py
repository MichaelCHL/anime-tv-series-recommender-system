from utils.logger import get_logger
from config.path import MODELS_DIR, FEATURE_DIR, RAW_DATA_DIR
from custom_exception import ModelLoadingException, SimilarityCalculationException
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import load_npz

import joblib
import pandas as pd
import numpy as np

logger = get_logger(__name__)

class SimilarityCalculator:
    def __init__(self, model_name, model_path=MODELS_DIR, feature_path=FEATURE_DIR):
        self.model_path = model_path
        self.model_name = model_name
        self.feature_path = feature_path
        self.feature_matrix=None
        
    def load_model(self):
        try:
            if self.model_name.lower() == 'tf-idf':
                logger.info("Loading tf-idf matrix...")

                self.feature_path = FEATURE_DIR
                matrix_path = self.feature_path / 'tfidf_matrix.npz'
                self.feature_matrix = load_npz(matrix_path)
                logger.info("tf-idf matrix loaded successfully!")

        except Exception as e:
            logger.error("Failed to load model!")
            raise ModelLoadingException("Failed to load model", e)

    def compute(self):
        try:
            logger.info("Calculating similarity...")
            sims = cosine_similarity(self.feature_matrix, self.feature_matrix).flatten()
            logger.info("Calculation completed!")
            return sims
        
        
        except Exception as e:
            logger.error("Failed to compute cosine similarity")
            raise SimilarityCalculationException("Failed to compute cosine similarity", e)

if __name__ == '__main__':
    sim_calculator = SimilarityCalculator('tf-idf')
    sim_calculator.load_model()
    sim_calculator.compute()
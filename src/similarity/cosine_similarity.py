from utils.logger import get_logger
from config.path import MODELS_DIR, FEATURE_DIR
from custom_exception import ModelLoadingException
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import load_npz

import joblib

logger = get_logger(__name__)

class SimilarityCalculator:
    def __init__(self, model_name, model_path=MODELS_DIR, feature_path=None):
        self.model_path = model_path
        self.model_name = model_name
        self.feature_path = feature_path
        self.model = None
        self.feature_matrix=None
        
    def load_model(self):
        try:
            if self.model_name.lower() == 'tf-idf':
                logger.info("Loading tf-idf matrix...")

                self.feature_path = FEATURE_DIR
                matrix_path = self.feature_matrix / 'tfidf.npz'
                self.feature_matrix = load_npz(matrix_path)

                logger.info("tf-idf matrix loaded successfully!")

        except Exception as e:
            logger.error("Failed to load model!")
            raise ModelLoadingException("Failed to load model", e)

    def recommend(self):
        try:
            logger.info("Recommending similar anime and tv series...")
            similarity_matrix = cosine_similarity(self.model, self.model)            
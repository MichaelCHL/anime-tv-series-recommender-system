from similarity.cosine_similarity import SimilarityCalculator
from utils.logger import get_logger
from custom_exception import RecommendationException

logger = get_logger(__name__)

class Recommender:
    def __init__(self):
        self.sim_calculator = SimilarityCalculator('tf-idf')
    
    def recommend(self, idx, k):
        try:
            logger.info("Recommending similar contents...")
            self.sim_calculator.load_model()
            sim = self.sim_calculator.compute()
            result = sorted(sim[idx])[1:k+1]
            logger.info("Recommending process completed!")
            return result
        except Exception as e:
            logger.error("Failed to recommend similar content")
            raise RecommendationException("Recommending process failed", e)
            ## continue on how to get anime names and index
            ## also think about how to present it on streamlit

if __name__ == '__main__':
    idx = input("Please enter the index for anime/tv series")
    k = input("Please enter the number of similar shows you would like to be recommended.")
    recommender = Recommender()
    results = recommender.recommend(idx, k)
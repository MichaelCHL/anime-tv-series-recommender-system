class PipelineException(Exception):
    def __init__(self, message, error_code):
        self.message = message
        super().__init__(self.message)
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"

class DataLoadingException(PipelineException):
    pass

class DataCleaningException(PipelineException):
    pass

class FeaturePreparationException(PipelineException):
    pass

class VectorizationException(PipelineException):
    pass

class ModelLoadingException(PipelineException):
    pass

class SimilarityCalculationException(PipelineException):
    pass

class RecommendationException(PipelineException):
    pass
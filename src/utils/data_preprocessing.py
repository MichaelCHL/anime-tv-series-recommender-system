import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

class Preprocessing:
    def __init__(self):
        

    def stopword_remove(synopsis):
        # get english stopwords and tokenize 
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(synopsis.lower())
        
        # remove stopwords
        filtered_tokens = [word for word in tokens if word not in stop_words]

        return filtered_tokens

    def year_conversion(date_str):
        year = re.findall(r"\b\d{4}\b", date_str)
        return year[0] if year else None


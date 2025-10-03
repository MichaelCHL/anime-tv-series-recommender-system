import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwrods')
nltk.download('punkt')

def stopword_remove(synopsis):
    
    # get english stopwords and tokenize 
    stop_words = set(stop_words.words('english'))
    tokens = word_tokenize(synopsis.lower())
    
    # remove stopwords
    filtered_tokens = [word for word in tokens if word not in stop_words]

    return filtered_tokens
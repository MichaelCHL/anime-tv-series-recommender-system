import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwrods')
nltk.download('punkt')

def text_cleaning(col):
    stop_words = set(stopwords.words('english'))
    clean_col = re.sub(r'[^a-zA-Z0-9\s]', '', col)
    tokens = word_tokenize(clean_col.lower())
    clean_txt = [word for word in tokens if word not in stop_words]

    return clean_txt


def find_year(col):
    year = re.findall(r"\b\d{4}\b", col)[0]
    return year[0] if year else None

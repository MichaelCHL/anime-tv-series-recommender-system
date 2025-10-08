import re
import shutil
import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# nltk_data_path = os.path.expanduser('~/nltk_data')
# punkt_tab_path = os.path.join(nltk_data_path, 'tokenizers', 'punkt_tab')
# if os.path.exists(punkt_tab_path):
#     shutil.rmtree(punkt_tab_path)

nltk.download('punkt')#, download_dir=nltk_data_path)
nltk.download('stopwords')#, download_dir=nltk_data_path)

def text_cleaning(col):
    stop_words = set(stopwords.words('english'))
    clean_col = re.sub(r'[^a-zA-Z0-9\s]', '', col)
    tokens = word_tokenize(clean_col.lower())
    clean_txt = [word for word in tokens if word not in stop_words]

    return clean_txt


def find_year(col):
    year = re.findall(r"\b\d{4}\b", col)
    return year[0] if year else None

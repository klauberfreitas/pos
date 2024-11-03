import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from nltk.tokenize import word_tokenize
import unicodedata
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('stopwords')
nltk.download('punkt')

def remove_accent(text):
    nfkd = unicodedata.normalize('NFKD', text)
    return u"".join([c for c in nfkd if not unicodedata.combining(c)])

def preprocess_text(text):
    text = remove_accent(text)
    
    text = text.lower()
    
    text = re.sub(r'[^\w\s]', '', text)
    
    tokens = word_tokenize(text)
    
    stop_words = set(stopwords.words('portuguese'))
    tokens = [word for word in tokens if word not in stop_words]

    stemmer = RSLPStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    return tokens

df = pd.read_csv('global-assets/datasets/b2w.csv')

df['processed_text'] = df['review_text'].apply(preprocess_text) 

all_tokens = [token for sublist in df['processed_text'] for token in sublist]

token_freq = Counter(all_tokens)

wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(token_freq)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
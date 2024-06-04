import numpy as np
import csv
import re
import contractions

from collections import Counter
from itertools import chain

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from tensorflow import keras

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def clean_text(text):
    text = contractions.fix(text)
    text = re.sub(r'[^a-zA-Z\s]', '', text) 
    text = text.lower()
    return text


def pp_text(docs):
    lemmatizer = WordNetLemmatizer() 
    stop_words = set(stopwords.words('english')) 

    processed_docs = []

    for doc in docs:
        cleaned_text = clean_text(doc)
        words = word_tokenize(cleaned_text)  
        words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
        processed_docs.append(" ".join(words))
    return processed_docs


reviews = []
sentiments = []

with open('imdb_dataset.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        reviews.append(row[0])
        sentiments.append(row[1])

cleaned_reviews = pp_text(reviews)

positive_reviews = [cleaned_reviews[i] for i in range(len(sentiments)) if sentiments[i] == 'positive']
negative_reviews = [cleaned_reviews[i] for i in range(len(sentiments)) if sentiments[i] == 'negative']

positive_words = list(chain(*[review.split() for review in positive_reviews]))
negative_words = list(chain(*[review.split() for review in negative_reviews]))

positive_word_counts = Counter(positive_words)
negative_word_counts = Counter(negative_words)


unique_positive_words = {word: count for word, count in positive_word_counts.items() if word not in negative_word_counts}
unique_negative_words = {word: count for word, count in negative_word_counts.items() if word not in positive_word_counts}

positive_wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(unique_positive_words) 
plt.figure(figsize=(10, 5))                                 # 시각화할 그림의 크기 설정 (가로, 세로)
plt.imshow(positive_wordcloud, interpolation='bilinear')    # 워드클라우드를 이미지로 표시, interpolation: 이미지 보간법 설정
plt.axis('off')                                             # x, y축 숫자 표시 여부 설정                     
plt.title('Positive Reviews WordCloud')
plt.savefig('positive_reviews_wordcloud.jpg')
plt.show()   

negative_wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(unique_negative_words)
plt.figure(figsize=(10, 5))
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Negative Reviews WordCloud')
plt.savefig('negative_reviews_wordcloud.jpg')
plt.show()



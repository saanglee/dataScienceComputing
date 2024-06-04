import re               # regular expression library
import contractions     # expanding contractions in English
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from collections import Counter
from itertools import chain

from tensorflow import keras            
from tensorflow.keras.preprocessing.text import Tokenizer           # 텍스트를 토큰화하여 각 단어를 특정 정수로 변환된 시퀀스로
from tensorflow.keras.perprocessing.sequence import pad_sequences   # 모든 시퀀스가 동일한 길이를 가지도록 패딩하는 함수

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder                      # 범주형 라벨을 수치 형식으로 변환

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer    

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

def clean_text(doc):
    text = re.sub(r'[^\w\s]', '', doc)  # 특수문자 제거(# 알파벳/숫자/밑줄/공백 제외 모든 문자 제거)
    text = contractions.fix(text)
    text = text.lower()

    words = nltk.word_tokenize(text)    # 문장을 단어로 쪼개기
    
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    clean_text = ' '.join(words)
    return clean_text

def pp_text(docs):
    return [clean_text(doc) for doc in docs]

categories = [                                                  # 20개의 뉴스그룹 중 6개의 뉴스그룹만 사용  
              'alt.atheism', 'talk.politics.misc', 'comp.graphics',
              'sci.med', 'rec.sport.baseball'
              ]

train_data = fetch_20newsgroups(subset='train', categories=categories, random_state=2023)
test_data = fetch_20newsgroups(subset='test', categories=categories, random_state=2023)

# preprocessing
train_docs = pp_text(train_data.data)
test_docs = pp_text(test_data.data)

vectorizer = TfidfVectorizer(max_feature=1000)
X_train = vectorizer.fit_transform(train_docs).toarray()
X_test = vectorizer.fit_transform(test_docs).toarray()

X_train, X_intermediate, y_train, y_intermediate = train_test_split(X_train, train_data.target, test_size=0.2, random_state=2023)
X_valid, X_test, y_valid, y_test = train_test_split(X_intermediate, y_intermediate, test_size=0.5, random_state=2023)


model = keras.models.Sequential()                     # Sequential 모델 생성
model.add(keras.layers.Flatten(input_shape=[1000]))   # Flatten 레이어 추가: 1000개의 특성을 가진 입력을 1차원 배열로 변환(평탄화)
model.add(keras.layers.Dense(256, activation="elu"))  # Dense 레이어 추가: 256개의 뉴런과 활성화 함수로 ELU(Exponential Linear Unit) 사용
model.add(keras.layers.Dense(128, activation="elu"))
model.add(keras.layers.Dense(64, activation="elu"))
model.add(keras.layers.Dense(5, activation="softmax"))  # 출력 레이어: 5개의 뉴런과 소프트맥스 활성화 함수 사용


model.compile(loss="sparse_categorical_crossentropy",   # 손실 함수로 희소 범주형 크로스 엔트로피 사용 - 이 손실 함수는 다중 클래스 분류 문제에서 사용
              optimizer="adam",                         # 옵티마이저로 Adam 사용 - Adam: 경사 하강법의 한 종류, 모델의 가중치를 업데이트
              metrics=["accuracy"])                     

history = model.fit(X_train, y_train, epochs=20,         
                    validation_data=(X_valid, y_valid))

loss, acc = model.evaluate(X_test, y_test)

print(f'The loss for test data is {loss:.2f}, and the accuracy is {acc:.2f}')
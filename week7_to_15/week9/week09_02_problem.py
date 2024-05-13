# -*- coding: utf-8 -*-
"""week09_02_problem.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18E1Lx6O7Rn0XPYtGNMFYfpX_fJRmsjCw
"""

# 라이브러리 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Machine-Learning에 필요한 라이브러리 import
import sklearn
from sklearn.model_selection import train_test_split

# 데이터 불러오기
titanic_df= pd.read_csv('titanic.csv')

"""Pandas DataFrame 참고 사이트

https://pandas.pydata.org/docs/reference/frame.html
"""

"""
Q1. age 결측치 확인 및 평균으로 채우기
"""

# check age missing value
print(titanic_df['Age'].isnull().sum())

# fill age missing value with mean
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)


"""
Q2. embarked 결측치를 확인하고 S로 채우기
"""

# check embarked missing value
print(titanic_df['Embarked'].isnull().sum())

# fill embarked missing value with 'S'
titanic_df['Embarked'].fillna('S', inplace=True)


########################

titanic_df['FamilySize'] = (titanic_df['SibSp'] + titanic_df['Parch'] + 1)
titanic_df['Alone'] = 0
titanic_df.loc[titanic_df['FamilySize'] == 1, 'Alone'] = 1
x1 = pd.get_dummies(titanic_df['Pclass'])
x2 = pd.get_dummies(titanic_df['Sex'])
x3 = pd.get_dummies(titanic_df['Embarked'])

data = pd.concat([titanic_df, x1, x2, x3], axis=1)

"""
Q3. 예측에 사용하지 않을 데이터를 제거하고, x, y 데이터를 나누기

제거 대상 컬럼 : 'PassengerId', 'Name', 'Ticket', 'Cabin', 'Survived', 'Pclass', 'Sex', 'Embarked'
"""
# delete unnecessary columns
data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Survived', 'Pclass', 'Sex', 'Embarked'], axis=1, inplace=True)

# split x, y data
x = data
y = titanic_df['Survived']


#### Your Code Here ####


########################

"""Scikit-learn "Logistic Regression" Document

https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

Scikit-learn "Cross_Validation_Score" Document

https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html
"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""
Q4. 주석을 참고하여 코드를 작성
"""

lr = LogisticRegression(max_iter=1000)

cv = cross_val_score(lr, x.values, y, cv=5, scoring='accuracy')

print(cv)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

print('X_train.shape:', X_train.shape)
print('y_train.shape:', y_train.shape)
print('X_test.shape:', X_test.shape)
print('y_test.shape:',y_test.shape)

"""
Q5. 주석을 참고해 모델을 학습시키고, 정확도를 구하기
"""
# train data 학습
lr.fit(X_train, y_train) 

# 예측 함수 작성
y_pred = lr.predict(X_test)
print('정확도:', accuracy_score(y_test, y_pred))

"""
Q6. 아래 값을 참고해서 my 변수를 완성하기

Age:26, SibSp: 1, Parch: 2, Fare: 100, FamilySize: 4, Alone: 0, Pclass: 2(0,1,0), Sex: male(0,1), Emb: C(1,0,0)

"""

my = [[
    26, # Age
    1, # SibSp
    2, # Parch
    100, # Fare
    4, # FamilySize
    0, # Alone
    0, # Pclass_1
    1, # Pclass_2
    0, # Pclass_3
    0, 
    1, 
    1,
    0,
    0
]]

pred = lr.predict(my)

if pred:
    print('생존!')
else:
    print('사망.')
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('titanic.csv')
df['Age'].isnull().sum()

age_mean = df['Age'].mean()
df['Age'].fillna(age_mean, inplace=True)

df['Embarked'].isnull().sum()
df['Embarked'].fillna('S', inplace=True)
df['FamilySize'] = (df['SibSp'] + df['Parch'] + 1)
df['Alone'] = 0

df.loc[df['FamilySize'] == 1, 'Alone'] == 1

# get_dummies(colname) one-hot encoding
x1 = pd.get_dummies(df['Pclass'])
x2 = pd.get_dummies(df['Sex'])
x3 = pd.get_dummies(df['Embarked'])

data = pd.concat([df,x1,x2,x3], axis=1)
data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Survived', 'Pclass', 'Sex', 'Embarked'], axis=1, inplace=True)

x = data
y = df['Survived']

lr = LogisticRegression()
cv = cross_val_score(lr, x.values, y, cv=5, scoring='accuracy')

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

print('X_train.shape:', X_train.shape)
print('y_train.shape:', y_train.shape)

lr.fit(X_train.values, y_train.values)
y_pred = lr.predict(X_test.values)

accuracy_score(y_test, y_pred)


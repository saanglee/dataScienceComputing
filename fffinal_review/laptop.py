# SVM, Naive Bayes, Decision Tree, K-neighbors, Random Forest

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

data = pd.read_csv('')
data.head()

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf_nb = GaussianNB()
y_pred_nb = clf_nb.fit(X_train, y_train).predict(X_test)
report_nb = classification_report(y_test, y_pred_nb)

clf_dt = DecisionTreeClassifier()
y_pred_dt = clf_dt.fit(X_train, y_train).predict(X_test)
report_dt = classification_report(y_test, y_pred_dt)

clf_rf = RandomForestClassifier()
y_pred_rf = clf_rf.fit(X_train, y_train).predict(X_test)
report_rf = classification_report(y_test,y_pred_rf)


clf_svm = SVC()
y_pred_svm = clf_svm.fit(X_train, y_train).predict(X_test)
report_svm = classification_report(y_test, y_pred_svm)

clf_kn = KNeighborsClassifier()
y_pred_kn = clf_kn.fit(X_train, y_train).predict(X_test)
report_kn = classification_report(y_test, y_pred_svm)






















"""
기존 출시된 폰 데이터
데이셋은 휴대폰 사양(배터리성능, 블투스가능여부, 듀얼심지원여부 등) 20가지와 
이에 따른 가격 범위 (0:낮은 가격, 1:중간 가격, 2:높은 가격, 3: 아주 높은 가격)

Decision Tree, K-neighbors, Random Forest 각각의 모델을 사용하여 
데이터를 훈련 및 예측해보고

Classification Report를 사용해 각 모델과 범위에 대해 성능을 평가하고
SVM모델의 정확도를 96 이상으로 올리기
"""


from sklearn.model_selection import train_test_split
from collections import Counter
import numpy as np
import pandas as pd

class ClassificationReport: # Classification Report를 사용해 각 모델과 범위에 대해 성능을 평가하고
    def __init__(self, num_class): 
        self.num_class = num_class

    def confusion_matrix(self, pred, target):
        cnfs_mat = [{'TP': 0, 'FP': 0, 'FN': 0, 'TN': 0} for _ in range(self.num_class)]
        for i in range(len(pred)):
            # Convert to int if target is a Pandas Series
            true_val = int(target.iloc[i]) if isinstance(target, pd.Series) else target[i]
            pred_val = int(pred[i]) if isinstance(pred, pd.Series) else pred[i]

            if pred_val == true_val:
                cnfs_mat[pred_val]['TP'] += 1
            else:
                cnfs_mat[pred_val]['FP'] += 1
                cnfs_mat[true_val]['FN'] += 1
                for j in range(self.num_class):
                    if j != pred_val and j != true_val:
                        cnfs_mat[j]['TN'] += 1
        return cnfs_mat

    # Precision은 TP (True Positive)를 TP + FP (False Positive)로 나눈 것
    def precision(self, TP, FP, FN, TN):
        prc = None
        if TP + FP != 0:
            prc = TP / (TP + FP)
        else:
            prc = 0

        return prc
    
    # Recall은 TP (True Positive)를 TP + FN (False Negative)로 나눈 것
    def recall(self, TP, FP, FN, TN): 
        rc = None
        if TP + FN != 0:
            rc = TP / (TP + FN)
        else:
            rc = 0

        return rc

    # F-measure는 Precision과 Recall의 조화평균
    def f_measure(self, precision, recall):
        fm = None
        #### Edit here ####
        # calculate f_measure
        if precision + recall != 0:
            fm = 2 * (precision * recall) / (precision + recall)
        else:
            fm = 0

        return fm

    def multiclass_evaluation(self, pred, target):
        # f_measure_, precision_, recall_ = [], [], []
        f_measure_, precision_, recall_, support_ = [], [], [], []
        
        cnfs_mat = self.confusion_matrix(pred, target)
        for i in range(self.num_class):
            TP = cnfs_mat[i]['TP']
            FP = cnfs_mat[i]['FP']
            FN = cnfs_mat[i]['FN']
            TN = cnfs_mat[i]['TN']
            precision_.append(self.precision(TP, FP, FN, TN))
            recall_.append(self.recall(TP, FP, FN, TN))
            f_measure_.append(self.f_measure(precision_[i], recall_[i])) 
            support_.append(TP + FN)  # Calculate support     
        accuracy_ = sum([cnfs_mat[i]['TP'] for i in range(self.num_class)]) / len(pred)

        # print column names
        print('Class   Precision   Recall   F-measure   Support')
        # 소수점 둘째자리까지 출력
        for i in range(self.num_class):
            # print(f'   {i}      {precision_[i]:.2f},      {recall_[i]:.2f},     {f_measure_[i]:.2f} ')
            print(f'   {i}      {precision_[i]:.2f},      {recall_[i]:.2f},     {f_measure_[i]:.2f},     {support_[i]}')
        print(f'Accuracy: {accuracy_:.2f}')
#### Edit here ####
# split the data into train-test data (train.csv) using train_test_split
# read the data from 'train.csv'
data = pd.read_csv('train.csv')
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# train each model using each model(SVM, Naive Bayes, Decision Tree, K-neighbors, Random Forest) and evaluate
# fix: test_size is 0.33, random_state is 2024
# use ClassificationReport class to evaluate the model
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=2024)
cr = ClassificationReport(4)

# Decision Tree
clf = tree.DecisionTreeClassifier()     # Decision Tree classifier 객체 생성
clf = clf.fit(X_train, y_train)         # classifier를 X_train, y_train 데이터를 이용해 학습 (X_train: feature, y_train: label), 학습된 classifier는 다시 clf에 저장됨
y_pred = clf.predict(X_test)            # clf 사용해 X_test 데이터에 대한 예측을 수행, 예측된 label은 y_pred에 저장됨
print('Decision Tree 분류 결과:')         
cr.multiclass_evaluation(y_pred, y_test) # y_pred 예측된 레이블, y_test 실제 레이블 # y_pred와 y_test 사용해 다중 클래스 평가 수행
                                         

# K-neighbors
clf = KNeighborsClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('K-neighbors 분류 결과:')
cr.multiclass_evaluation(y_pred, y_test)


# SVM
clf = SVC(kernel='linear', C=1)
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('SVM 분류 결과:')
cr.multiclass_evaluation(y_pred, y_test)

# Random Forest
clf = RandomForestClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('Random Forest 분류 결과:')
cr.multiclass_evaluation(y_pred, y_test)


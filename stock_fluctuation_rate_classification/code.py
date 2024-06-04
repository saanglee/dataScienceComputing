import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer            # SimpleImputer: 결측값을 특정 값(평균, 중앙값 등)으로 대체
from sklearn.preprocessing import OneHotEncoder

# Load datasets
train_path = './data/train.csv'
test_path = './data/test.csv'
sample_submission_path = './data/sample_submission.csv'

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)
sample_submission_df = pd.read_csv(sample_submission_path)

train_df.head(5)
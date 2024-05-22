import pandas as pd

# Load data
train_data = pd.read_csv('./data/train.csv')
test_data = pd.read_csv('./data/test.csv')
sample_submission = pd.read_csv('./data/sample_submission.csv')

# Check data
print(train_data.head())
print(test_data.head())
print(sample_submission.head())

# Preprocessing
# Check missing values
print(train_data.isnull().sum())
print(test_data.isnull().sum())

# Drop missing values
train_data = train_data.dropna()
test_data = test_data.dropna()

# Check missing values again
print(train_data.isnull().sum())
print(test_data.isnull().sum())
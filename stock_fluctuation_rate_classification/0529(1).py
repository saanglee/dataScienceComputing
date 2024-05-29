import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the datasets
train_path = './data/train.csv'
test_path = './data/test.csv'
sample_submission_path = './data/sample_submission.csv'

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)
sample_submission_df = pd.read_csv(sample_submission_path)

# Display the first few rows of the train dataset
train_df.head()

# Data preprocessing
# Extract features and target
X = train_df.drop(['id', 'label'], axis=1)
y = train_df['label']

# Standardize the feature values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the training data for validation
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a RandomForest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Validate the model
y_pred = model.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
print(f'Validation Accuracy: {accuracy:.4f}')

# Prepare the test data
test_ids = test_df['id']
X_test = test_df.drop(['id'], axis=1)
X_test_scaled = scaler.transform(X_test)

# Predict the labels for the test data
test_predictions = model.predict(X_test)

# Create the submission file
submission_df = pd.DataFrame({
    'id': test_ids,
    'label': test_predictions
})

# Save the submission file
submission_df.to_csv('./data/submission.csv', index=False)

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

# Load the datasets
train_df = pd.read_csv('./data/train.csv')
test_df = pd.read_csv('./data/test.csv')
sample_submission_df = pd.read_csv('./data/sample_submission.csv')

# Data preprocessing
# Extract features and target
X = train_df.drop(['id', 'label'], axis=1)
y = train_df['label']

# Handle missing values by imputing with mean
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Standardize the feature values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# Split the training data for validation
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a RandomForest Classifier with hyperparameter tuning
param_grid_rf = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

grid_search_rf = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
                              param_grid=param_grid_rf,
                              cv=3,
                              n_jobs=-1,
                              verbose=2)

grid_search_rf.fit(X_train, y_train)
best_model_rf = grid_search_rf.best_estimator_

# Validate the RandomForest model
y_pred_rf = best_model_rf.predict(X_val)
accuracy_rf = accuracy_score(y_val, y_pred_rf)
print(f'RandomForest Validation Accuracy: {accuracy_rf:.4f}')

# Train an XGBoost Classifier with hyperparameter tuning
param_grid_xgb = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.8, 1.0]
}

grid_search_xgb = GridSearchCV(estimator=xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss', random_state=42),
                               param_grid=param_grid_xgb,
                               cv=3,
                               n_jobs=-1,
                               verbose=2)

grid_search_xgb.fit(X_train, y_train)
best_model_xgb = grid_search_xgb.best_estimator_

# Validate the XGBoost model
y_pred_xgb = best_model_xgb.predict(X_val)
accuracy_xgb = accuracy_score(y_val, y_pred_xgb)
print(f'XGBoost Validation Accuracy: {accuracy_xgb:.4f}')

# Choose the best model based on validation accuracy
if accuracy_rf > accuracy_xgb:
    best_model = best_model_rf
    print("Selected model: RandomForest")
else:
    best_model = best_model_xgb
    print("Selected model: XGBoost")

# Prepare the test data
test_ids = test_df['id']
X_test = test_df.drop(['id'], axis=1)

# Handle missing values in the test set
X_test_imputed = imputer.transform(X_test)

# Standardize the test data
X_test_scaled = scaler.transform(X_test_imputed)

# Predict the labels for the test data using the selected model
test_predictions = best_model.predict(X_test_scaled)

# Create the submission file
submission_df = pd.DataFrame({
    'id': test_ids,
    'label': test_predictions
})

# Save the submission file
submission_file_path = 'submission.csv'
submission_df.to_csv(submission_file_path, index=False)

# Display the submission file path and best validation accuracy
print(f'Submission file created: {submission_file_path}')
print(f'Best Validation Accuracy: {max(accuracy_rf, accuracy_xgb):.4f}')

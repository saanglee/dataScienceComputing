import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import lightgbm as lgb
from xgboost import XGBClassifier

# Load datasets
train_path = './data/train.csv'
test_path = './data/test.csv'
sample_submission_path = './data/sample_submission.csv'

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)
sample_submission_df = pd.read_csv(sample_submission_path)

# Feature Engineering - Create new features or transformations if necessary
def feature_engineering(df):
    df = df.copy()
    # Example: Create a feature that is the log of a numeric column (assuming 'price' exists)
    if 'price' in df.columns:
        df['log_price'] = np.log1p(df['price'])
    return df

train_df = feature_engineering(train_df)
test_df = feature_engineering(test_df)

# Preprocessing
numeric_features = train_df.select_dtypes(include=['int64', 'float64']).columns.tolist()
numeric_features.remove('label')  # Exclude target column

categorical_features = train_df.select_dtypes(include=['object']).columns.tolist()

# Define column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ]), numeric_features),
        ('cat', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ]), categorical_features)
    ])

# Split features and target
X = train_df.drop('label', axis=1)
y = train_df['label']

# Split into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Model pipeline for RandomForest
rf_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Model pipeline for GradientBoosting
gb_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', GradientBoostingClassifier(random_state=42))
])

# Model pipeline for XGBoost
xgb_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', XGBClassifier(random_state=42))
])

# Model pipeline for LightGBM
lgb_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', lgb.LGBMClassifier(random_state=42))
])

# Hyperparameter tuning
param_grid_rf = {
    'classifier__n_estimators': [100, 200, 300],
    'classifier__max_depth': [None, 10, 20, 30],
    'classifier__min_samples_split': [2, 5, 10],
    'classifier__min_samples_leaf': [1, 2, 4]
}

param_grid_gb = {
    'classifier__n_estimators': [100, 200],
    'classifier__learning_rate': [0.01, 0.1, 0.2],
    'classifier__max_depth': [3, 5, 7]
}

param_grid_xgb = {
    'classifier__n_estimators': [100, 200],
    'classifier__learning_rate': [0.01, 0.1, 0.2],
    'classifier__max_depth': [3, 5, 7]
}

param_grid_lgb = {
    'classifier__n_estimators': [100, 200],
    'classifier__learning_rate': [0.01, 0.1, 0.2],
    'classifier__num_leaves': [31, 40, 50]
}

# Define cross-validation strategy
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Perform grid search for each model
grid_search_rf = GridSearchCV(rf_model, param_grid_rf, cv=cv, scoring='accuracy', n_jobs=-1)
grid_search_rf.fit(X_train, y_train)

grid_search_gb = GridSearchCV(gb_model, param_grid_gb, cv=cv, scoring='accuracy', n_jobs=-1)
grid_search_gb.fit(X_train, y_train)

grid_search_xgb = GridSearchCV(xgb_model, param_grid_xgb, cv=cv, scoring='accuracy', n_jobs=-1)
grid_search_xgb.fit(X_train, y_train)

grid_search_lgb = GridSearchCV(lgb_model, param_grid_lgb, cv=cv, scoring='accuracy', n_jobs=-1)
grid_search_lgb.fit(X_train, y_train)

# Retrieve the best models
best_rf = grid_search_rf.best_estimator_
best_gb = grid_search_gb.best_estimator_
best_xgb = grid_search_xgb.best_estimator_
best_lgb = grid_search_lgb.best_estimator_

# Ensemble model using voting classifier
ensemble_model = VotingClassifier(estimators=[
    ('rf', best_rf),
    ('gb', best_gb),
    ('xgb', best_xgb),
    ('lgb', best_lgb)
], voting='soft')

ensemble_model.fit(X_train, y_train)

# Validation
y_val_pred = ensemble_model.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
print(f'Validation Accuracy: {val_accuracy}')

# Predictions on test set
test_predictions = ensemble_model.predict(test_df)

# Prepare submission
submission_df = sample_submission_df.copy()
submission_df['label'] = test_predictions
submission_df['label'] = submission_df['label'].astype(int)

# Save submission
submission_df.to_csv('./data/submission.csv', index=False)
print("Submission file saved as 'submission.csv'")

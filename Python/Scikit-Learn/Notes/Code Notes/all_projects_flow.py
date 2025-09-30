# =========================================
# 1. IMPORT LIBRARIES
# =========================================
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.cluster import KMeans

# =========================================
# 2. LOAD / UPLOAD DATASET
# =========================================
# Local CSV
data = pd.read_csv("dataset.csv")

# OR upload file (if using Google Colab, Kaggle, Jupyter)
# from google.colab import files
# uploaded = files.upload()

# =========================================
# 3. UNDERSTAND THE DATA
# =========================================
print(data.head())        # check first 5 rows
print(data.info())        # check datatypes
print(data.describe())    # check summary stats
print(data.isnull().sum())# check missing values
print(data['target'].value_counts())  # for classification

# =========================================
# 4. PREPROCESSING (Cleaning + Feature Engineering)
# =========================================
# - Handle missing values
# - Encode categorical variables (LabelEncoder / OneHotEncoder)
# - Scale numeric features (StandardScaler / MinMaxScaler)
# - Feature selection if needed

# Example: split categorical + numeric
cat_cols = ['gender', 'occupation']
num_cols = ['age', 'income']

# Define preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(), cat_cols)
    ]
)

# =========================================
# 5. SPLIT INTO TRAIN & TEST SETS
# =========================================
X = data.drop("target", axis=1)
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================================
# 6. CHOOSE ML APPROACH (depends on problem type)
# =========================================
# A. Classification -> Predict discrete labels (Yes/No, Spam/Not Spam)
classifier = RandomForestClassifier()

# B. Regression -> Predict continuous values (Price, Temperature)
regressor = LinearRegression()

# C. Clustering -> Group data without labels (Customer Segmentation)
clusterer = KMeans(n_clusters=3)

# =========================================
# 7. CREATE PIPELINE (Preprocessing + Model)
# =========================================
clf_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('model', classifier)])

reg_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('model', regressor)])

# =========================================
# 8. TRAIN MODEL
# =========================================
clf_pipeline.fit(X_train, y_train)  # for classification
reg_pipeline.fit(X_train, y_train)  # for regression

# =========================================
# 9. PREDICT
# =========================================
y_pred_clf = clf_pipeline.predict(X_test)   # classification
y_pred_reg = reg_pipeline.predict(X_test)   # regression

# =========================================
# 10. EVALUATE PERFORMANCE
# =========================================
# Classification
print("Accuracy:", accuracy_score(y_test, y_pred_clf))

# Regression
print("MSE:", mean_squared_error(y_test, y_pred_reg))

# =========================================
# 11. IMPROVE (Tuning, Cross-validation, Feature Engineering)
# =========================================
# - Use GridSearchCV / RandomizedSearchCV
# - Try different models (SVM, XGBoost, Neural Nets)
# - Add/remove features
# - Collect more data

# =========================================
# 12. DEPLOY / SAVE MODEL
# =========================================
import joblib
joblib.dump(clf_pipeline, "model.pkl")   # save model
# Later: model = joblib.load("model.pkl") # load model

# Deploy: Flask API, FastAPI, Streamlit, Django, etc.

# =========================================
# MACHINE LEARNING PROJECT FLOW
# =========================================
# Every ML project follows this core flow:
# 1. Import libraries
# 2. Load/upload data
# 3. Explore & clean data
# 4. Preprocess features
# 5. Split train/test
# 6. Pick algorithm (classification, regression, clustering, etc.)
# 7. Train model
# 8. Predict
# 9. Evaluate
# 10. Improve (tuning, new features)
# 11. Save & Deploy
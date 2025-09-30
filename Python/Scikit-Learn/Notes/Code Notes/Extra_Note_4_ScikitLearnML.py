"""
=================================================================
SCIKIT-LEARN & MACHINE LEARNING - Comprehensive Guide
=================================================================

This file covers essential machine learning concepts:
- Supervised learning fundamentals
- Train-test split
- Data preprocessing (imputation, scaling, encoding)
- Cross-validation
- Model evaluation
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# =================================================================
# 1. SUPERVISED LEARNING FUNDAMENTALS
# =================================================================
print("=" * 60)
print("1. SUPERVISED LEARNING - CORE CONCEPTS")
print("=" * 60)

print("""
SUPERVISED LEARNING:
- Goal: Train a model to predict outcomes based on labeled data
- "Supervised" = learning from examples with known answers
- Training data has features (X) and labels/targets (y)

Types:
1. Classification: Predict categories (spam/not spam, cat/dog)
2. Regression: Predict continuous values (price, temperature)

Process:
1. Collect labeled training data
2. Train model on this data
3. Model learns patterns
4. Use model to predict new, unseen data

Example Applications:
- Email spam detection (classification)
- House price prediction (regression)
- Image recognition (classification)
- Stock price forecasting (regression)
""")


# =================================================================
# 2. TRAIN-TEST SPLIT
# =================================================================
print("=" * 60)
print("2. TRAIN-TEST SPLIT - DATA SPLITTING")
print("=" * 60)

# Create sample dataset
np.random.seed(42)
X = np.random.rand(100, 5)  # 100 samples, 5 features
y = np.random.randint(0, 2, 100)  # Binary classification

print("Original dataset shape:", X.shape)
print("Target shape:", y.shape)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,    # 20% for testing
    random_state=42   # Reproducibility
)

print(f"\nAfter split:")
print(f"Training set: {X_train.shape} (80%)")
print(f"Test set: {X_test.shape} (20%)")

print("""
WHY SPLIT DATA?
- Training set: Teach the model patterns
- Test set: Evaluate on UNSEEN data (unbiased evaluation)
- Prevents overfitting detection
- Simulates real-world deployment

PARAMETERS:
- test_size: Proportion for test set (0.2 = 20%)
- random_state: Seed for reproducibility (same split every time)
- stratify: Maintain class distribution (for imbalanced data)
""")

# Example with stratification
X_train_strat, X_test_strat, y_train_strat, y_test_strat = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nClass distribution:")
print(f"Original: {np.bincount(y)}")
print(f"Train (stratified): {np.bincount(y_train_strat)}")
print(f"Test (stratified): {np.bincount(y_test_strat)}")


# =================================================================
# 3. HANDLING MISSING VALUES - SIMPLEIMPUTER
# =================================================================
print("\n" + "=" * 60)
print("3. HANDLING MISSING VALUES WITH SIMPLEIMPUTER")
print("=" * 60)

# Create dataset with missing values
data_with_missing = pd.DataFrame({
    'feature1': [1, 2, None, 4, 5, None, 7, 8],
    'feature2': [10, None, 30, 40, None, 60, 70, 80],
    'feature3': [100, 200, 300, None, 500, 600, None, 800]
})

print("Original data with missing values:")
print(data_with_missing)
print(f"\nMissing values per column:\n{data_with_missing.isna().sum()}")

# Strategy 1: Mean imputation
imputer_mean = SimpleImputer(strategy='mean')
data_mean = imputer_mean.fit_transform(data_with_missing)
print("\n--- After MEAN imputation ---")
print(pd.DataFrame(data_mean, columns=data_with_missing.columns))

# Strategy 2: Median imputation (better for skewed data)
imputer_median = SimpleImputer(strategy='median')
data_median = imputer_median.fit_transform(data_with_missing)
print("\n--- After MEDIAN imputation ---")
print(pd.DataFrame(data_median, columns=data_with_missing.columns))

# Strategy 3: Most frequent (for categorical data)
categorical_data = pd.DataFrame({
    'color': ['red', 'blue', None, 'red', None, 'blue', 'green']
})
imputer_freq = SimpleImputer(strategy='most_frequent')
data_freq = imputer_freq.fit_transform(categorical_data)
print("\n--- Most Frequent imputation (categorical) ---")
print(f"Original: {categorical_data['color'].tolist()}")
print(f"Imputed: {data_freq.flatten().tolist()}")

# Strategy 4: Constant value
imputer_const = SimpleImputer(strategy='constant', fill_value=0)
data_const = imputer_const.fit_transform(data_with_missing)
print("\n--- Constant value (0) imputation ---")
print(pd.DataFrame(data_const, columns=data_with_missing.columns))

print("""
IMPUTATION STRATEGIES:
1. 'mean': Average of non-missing values (numeric)
2. 'median': Middle value (better for outliers)
3. 'most_frequent': Most common value (categorical)
4. 'constant': Specific value (fill_value parameter)

WHEN TO USE EACH:
- Mean: Normally distributed numeric data
- Median: Skewed numeric data, presence of outliers
- Most frequent: Categorical variables
- Constant: Domain-specific default (e.g., 0 for counts)
""")


# =================================================================
# 4. FEATURE SCALING - MINMAXSCALER
# =================================================================
print("\n" + "=" * 60)
print("4. FEATURE SCALING WITH MINMAXSCALER")
print("=" * 60)

# Create sample data with different scales
data = pd.DataFrame({
    'age': [25, 30, 35, 40, 45],
    'salary': [50000, 60000, 70000, 80000, 90000],
    'years_exp': [2, 5, 7, 10, 12]
})

print("Original data (different scales):")
print(data)
print("\nNotice the different ranges:")
print(f"Age: {data['age'].min()} - {data['age'].max()}")
print(f"Salary: {data['salary'].min()} - {data['salary'].max()}")
print(f"Years: {data['years_exp'].min()} - {data['years_exp'].max()}")

# MinMaxScaler: Scale to range [0, 1]
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

print("\n--- After MinMaxScaler (0 to 1) ---")
print(pd.DataFrame(data_scaled, columns=data.columns))

print("\nFormula: X_scaled = (X - X_min) / (X_max - X_min)")
print("\nVerification for 'age' column:")
age_min, age_max = data['age'].min(), data['age'].max()
age_scaled_manual = (data['age'] - age_min) / (age_max - age_min)
print(f"Manual calculation: {age_scaled_manual.tolist()}")

# Alternative: StandardScaler (mean=0, std=1)
from sklearn.preprocessing import StandardScaler
scaler_std = StandardScaler()
data_standardized = scaler_std.fit_transform(data)

print("\n--- StandardScaler (mean=0, std=1) ---")
print(pd.DataFrame(data_standardized, columns=data.columns))

print("""
WHY SCALE FEATURES?
- Algorithms like SVM, KNN sensitive to feature magnitudes
- Prevents features with large values from dominating
- Speeds up gradient descent convergence
- Required for distance-based algorithms

MinMaxScaler: Scales to [0, 1]
- Good when you need bounded values
- Preserves zero values
- Sensitive to outliers

StandardScaler: Scales to mean=0, std=1
- Less sensitive to outliers
- Commonly used in deep learning
- Better for normally distributed data
""")


# =================================================================
# 5. K-FOLD CROSS-VALIDATION
# =================================================================
print("\n" + "=" * 60)
print("5. K-FOLD CROSS-VALIDATION")
print("=" * 60)

# Create sample dataset
np.random.seed(42)
X = np.random.rand(50, 3)
y = np.random.randint(0, 2, 50)

print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features")

# Set up 5-fold cross-validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

print("\nK-Fold splits:")
for fold, (train_idx, test_idx) in enumerate(kfold.split(X), 1):
    print(f"Fold {fold}:")
    print(f"  Train indices: {len(train_idx)} samples")
    print(f"  Test indices: {len(test_idx)} samples")
    print(f"  Test indices: {test_idx[:5]}... (showing first 5)")

# Train model with cross-validation
model = LogisticRegression(random_state=42, max_iter=1000)

# Method 1: Manual cross-validation
fold_scores = []
for fold, (train_idx, test_idx) in enumerate(kfold.split(X), 1):
    X_train_fold = X[train_idx]
    X_test_fold = X[test_idx]
    y_train_fold = y[train_idx]
    y_test_fold = y[test_idx]
    
    model.fit(X_train_fold, y_train_fold)
    score = model.score(X_test_fold, y_test_fold)
    fold_scores.append(score)
    print(f"\nFold {fold} Accuracy: {score:.3f}")

print(f"\nAverage Accuracy: {np.mean(fold_scores):.3f}")
print(f"Standard Deviation: {np.std(fold_scores):.3f}")

# Method 2: Using cross_val_score (easier!)
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"\nUsing cross_val_score:")
print(f"Scores: {scores}")
print(f"Mean: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")

print("""
K-FOLD CROSS-VALIDATION:
- Split data into K equal parts (folds)
- Train on K-1 folds, test on remaining fold
- Repeat K times, each fold used as test once
- Average the K scores

BENEFITS:
- More reliable performance estimate
- Uses all data for both training and testing
- Reduces variance in performance estimate
- Detects overfitting

PARAMETERS:
- n_splits: Number of folds (typically 5 or 10)
- shuffle: Randomize data before splitting
- random_state: Reproducibility
""")


# =================================================================
# 6. CROSS_VAL_SCORE WITH DIFFERENT METRICS
# =================================================================
print("\n" + "=" * 60)
print("6. CROSS-VALIDATION WITH DIFFERENT SCORING METRICS")
print("=" * 60)

# Create imbalanced dataset
np.random.seed(42)
X = np.random.rand(100, 5)
y = np.concatenate([np.ones(80), np.zeros(20)])  # Imbalanced

model = RandomForestClassifier(random_state=42, n_estimators=50)

# Different scoring metrics
metrics = ['accuracy', 'precision', 'recall', 'f1']

print("Evaluating with different metrics:")
for metric in metrics:
    scores = cross_val_score(model, X, y, cv=5, scoring=metric)
    print(f"\n{metric.upper()}:")
    print(f"  Scores: {scores}")
    print(f"  Mean: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")

print("""
SCORING METRICS:
- 'accuracy': (TP + TN) / Total
  Good for balanced datasets

- 'precision': TP / (TP + FP)
  "Of predicted positives, how many are correct?"
  Important when false positives are costly

- 'recall': TP / (TP + FN)
  "Of actual positives, how many did we find?"
  Important when false negatives are costly

- 'f1': Harmonic mean of precision and recall
  Balance between precision and recall
  Good for imbalanced datasets

TP = True Positive, TN = True Negative
FP = False Positive, FN = False Negative
""")


# =================================================================
# 7. COMPLETE PREPROCESSING PIPELINE
# =================================================================
print("\n" + "=" * 60)
print("7. COMPLETE PREPROCESSING PIPELINE EXAMPLE")
print("=" * 60)

# Create realistic messy dataset
np.random.seed(42)
df = pd.DataFrame({
    'age': [25, None, 35, 40, None, 50, 55],
    'income': [50000, 60000, None, 80000, 70000, None, 95000],
    'score': [75, 82, 88, None, 91, 85, 94],
    'purchased': [0, 1, 1, 1, 0, 1, 1]
})

print("Original messy data:")
print(df)

# Step 1: Separate features and target
X = df.drop('purchased', axis=1)
y = df['purchased']

# Step 2: Handle missing values
imputer = SimpleImputer(strategy='median')
X_imputed = imputer.fit_transform(X)

print("\nAfter imputation:")
print(pd.DataFrame(X_imputed, columns=X.columns))

# Step 3: Scale features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_imputed)

print("\nAfter scaling (0-1):")
print(pd.DataFrame(X_scaled, columns=X.columns))

# Step 4: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

# Step 5: Train model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Step 6: Evaluate
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"\n Model Performance:")
print(f"Training accuracy: {train_score:.3f}")
print(f"Test accuracy: {test_score:.3f}")

# Step 7: Cross-validation
cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='accuracy')
print(f"Cross-validation: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")

print("""
PREPROCESSING PIPELINE:
1. Separate features (X) and target (y)
2. Handle missing values (SimpleImputer)
3. Scale features (MinMaxScaler)
4. Split data (train_test_split)
5. Train model
6. Evaluate on test set
7. Cross-validate for robust estimate

This ensures:
- Clean, consistent data
- Fair comparison between features
- Unbiased evaluation
- Robust performance estimates
""")


# =================================================================
# SUMMARY
# =================================================================
print("\n" + "=" * 60)
print("SUMMARY - SCIKIT-LEARN & MACHINE LEARNING")
print("=" * 60)
print("""
KEY CONCEPTS:

1. Supervised Learning:
   - Learn from labeled data
   - Predict on new data
   
2. Train-Test Split:
   train_test_split(X, y, test_size=0.2, random_state=42)
   - Unbiased evaluation
   
3. Missing Values:
   SimpleImputer(strategy='mean'/'median'/'most_frequent')
   - Clean data before modeling
   
4. Feature Scaling:
   MinMaxScaler() → [0, 1]
   StandardScaler() → mean=0, std=1
   - Equal feature importance
   
5. Cross-Validation:
   KFold(n_splits=5)
   cross_val_score(model, X, y, cv=5, scoring='accuracy')
   - Robust performance estimate

WORKFLOW:
Raw Data → Clean → Scale → Split → Train → Evaluate → Validate
""")
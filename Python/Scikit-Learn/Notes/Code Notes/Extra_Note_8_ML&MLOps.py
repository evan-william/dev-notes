"""
Machine Learning & MLOps Fundamentals
======================================
This file covers essential ML preprocessing, model operations, and MLOps concepts
for building and deploying machine learning systems.
"""

import numpy as np
import pandas as pd
import requests
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

# =============================================================================
# DATA NORMALIZATION WITH MINMAXSCALER
# =============================================================================

print("=" * 60)
print("NORMALIZING DATA TO RANGE [0, 1]")
print("=" * 60)

# MinMaxScaler transforms features to a range between 0 and 1
# Formula: X_scaled = (X - X_min) / (X_max - X_min)
# This is useful when features have different scales/units

# Example: Different scale features
raw_data = np.array([
    [100, 5, 20],    # Row 1: income, age, items_purchased
    [200, 35, 50],   # Row 2
    [150, 45, 30],   # Row 3
    [50, 25, 10]     # Row 4
])

print(f"Original data (different scales):\n{raw_data}\n")
print(f"Column 1 range: {raw_data[:, 0].min()} - {raw_data[:, 0].max()}")
print(f"Column 2 range: {raw_data[:, 1].min()} - {raw_data[:, 1].max()}")
print(f"Column 3 range: {raw_data[:, 2].min()} - {raw_data[:, 2].max()}\n")

# Initialize and fit the scaler
scaler = MinMaxScaler()
# fit() learns the min and max from the data
# transform() applies the scaling
normalized_data = scaler.fit_transform(raw_data)

print(f"Normalized data (range [0, 1]):\n{normalized_data}\n")
print(f"All values now between 0 and 1!")
print(f"Min value: {normalized_data.min():.4f}")
print(f"Max value: {normalized_data.max():.4f}\n")

# IMPORTANT: For train/test split, fit on training data only!
print("=" * 60)
print("PROPER TRAIN/TEST SCALING")
print("=" * 60)

X_train = np.array([[100, 20], [200, 40], [150, 30]])
X_test = np.array([[180, 35], [120, 25]])

print(f"Training data:\n{X_train}")
print(f"Test data:\n{X_test}\n")

# Create scaler and fit ONLY on training data
scaler_train = MinMaxScaler()
X_train_scaled = scaler_train.fit_transform(X_train)  # fit + transform
X_test_scaled = scaler_train.transform(X_test)        # only transform

print(f"Scaled training data:\n{X_train_scaled}")
print(f"Scaled test data:\n{X_test_scaled}\n")

print("WHY? We don't want information from test data to leak into training!")
print("The scaler must learn parameters (min, max) from training data only.\n")

# =============================================================================
# ONE-HOT ENCODING FOR CATEGORICAL FEATURES
# =============================================================================

print("=" * 60)
print("CONVERTING CATEGORICAL FEATURES TO NUMERICAL FORMAT")
print("=" * 60)

# OneHotEncoder converts categories into binary columns
# Each category becomes a separate column with 1 (present) or 0 (absent)

# Example: Converting colors to numerical format
colors = np.array([
    ['red'],
    ['blue'],
    ['green'],
    ['red'],
    ['blue']
])

print(f"Original categorical data:\n{colors}\n")

# Initialize OneHotEncoder
# sparse_output=False returns a regular numpy array instead of sparse matrix
encoder = OneHotEncoder(sparse_output=False)

# Fit and transform the data
colors_encoded = encoder.fit_transform(colors)

print(f"One-hot encoded data:\n{colors_encoded}")
print(f"Categories: {encoder.categories_}\n")
print("Column meanings: [blue, green, red]")
print("Row 1 [1, 0, 0] means: blue=1, green=0, red=0 → 'red' in original")
print("Notice the order!\n")

# Multi-column example with pandas
print("=" * 60)
print("ONE-HOT ENCODING MULTIPLE COLUMNS")
print("=" * 60)

# Create a sample dataset
data_df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'red', 'blue'],
    'size': ['small', 'large', 'medium', 'small', 'large'],
    'price': [10, 20, 15, 12, 18]
})

print(f"Original DataFrame:\n{data_df}\n")

# Use pd.get_dummies() for easier pandas one-hot encoding
encoded_df = pd.get_dummies(data_df, columns=['color', 'size'])

print(f"After one-hot encoding:\n{encoded_df}\n")

# =============================================================================
# LABEL ENCODING
# =============================================================================

print("=" * 60)
print("LABEL ENCODING: CONVERTING CATEGORIES TO INDICES")
print("=" * 60)

# Label encoding assigns an integer to each category
# Common approach: find the INDEX of a category within a list of unique categories

# Example categories
categories = ['cat', 'dog', 'bird', 'cat', 'dog', 'bird', 'cat']
print(f"Original categories: {categories}\n")

# Get unique categories
unique_categories = sorted(list(set(categories)))  # ['bird', 'cat', 'dog']
print(f"Unique categories (sorted): {unique_categories}\n")

# Create mapping: category -> index
category_to_index = {cat: idx for idx, cat in enumerate(unique_categories)}
print(f"Category to index mapping: {category_to_index}\n")

# Convert categories to indices
encoded_labels = [category_to_index[cat] for cat in categories]
print(f"Encoded labels: {encoded_labels}")
print("bird=0, cat=1, dog=2\n")

# Using sklearn's LabelEncoder (more robust)
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
encoded_sklearn = label_encoder.fit_transform(categories)

print(f"Using sklearn LabelEncoder: {encoded_sklearn}")
print(f"Classes: {label_encoder.classes_}\n")

# Decode back to original labels
decoded = label_encoder.inverse_transform(encoded_sklearn)
print(f"Decoded back: {list(decoded)}\n")

# =============================================================================
# WORKING WITH LLAMA AND PROMPT ENGINEERING
# =============================================================================

print("=" * 60)
print("LLAMA MODEL INFERENCE AND PROMPT STRUCTURE")
print("=" * 60)

# When performing inference with pre-trained models like Llama,
# the STRUCTURE OF THE INPUT PROMPT is the most critical factor

# Example of a well-structured prompt for Llama
prompt_example = """
<s>[INST] <<SYS>>
You are a helpful AI assistant specialized in answering questions about machine learning.
<</SYS>>

What is the difference between supervised and unsupervised learning? [/INST]
"""

print("Good prompt structure includes:")
print("1. Special tokens (<s>, [INST], <<SYS>>)")
print("2. System message defining the assistant's role")
print("3. Clear user instruction")
print("4. Proper closing tags\n")

print("Example well-structured prompt:")
print(prompt_example)

print("=" * 60)
print("FINE-TUNING LARGE LANGUAGE MODELS")
print("=" * 60)

print("""
Large Language Models like Llama3 are fine-tuned for specific use cases by:
→ CONTINUING THEIR TRAINING ON A NEW, SPECIALIZED DATASET

Fine-tuning process:
1. Start with a pre-trained model (e.g., Llama3-base)
2. Prepare a domain-specific dataset (e.g., medical texts, legal documents)
3. Continue training with a lower learning rate
4. The model adapts to the new domain while retaining general knowledge

Example use cases:
- Medical diagnosis: Fine-tune on medical literature
- Legal analysis: Fine-tune on legal documents
- Customer support: Fine-tune on support ticket data
- Code generation: Fine-tune on programming examples
""")

# =============================================================================
# FETCHING DATA FROM APIs
# =============================================================================

print("=" * 60)
print("FETCHING AND PARSING JSON DATA FROM APIs")
print("=" * 60)

# requests.get() fetches data from a URL
# .json() method parses the JSON response

# Example API endpoint (hypothetical)
api_url = "https://api.example.com/data"

print(f"Fetching data from: {api_url}\n")
print("Code structure:")
print("""
import requests

# Make GET request to API
response = requests.get(api_url)

# Check if request was successful
if response.status_code == 200:
    # Parse JSON data
    data = response.json()
    print(f"Data retrieved: {data}")
else:
    print(f"Error: {response.status_code}")
""")

# Simulated API response
simulated_response = [
    {"id": 1, "name": "Alice", "age": 30, "city": "New York"},
    {"id": 2, "name": "Bob", "age": 25, "city": "San Francisco"},
    {"id": 3, "name": "Charlie", "age": 35, "city": "Chicago"}
]

print("\nExample: Loading JSON data into pandas DataFrame\n")

# Method 1: Using pd.DataFrame.from_records()
df1 = pd.DataFrame.from_records(simulated_response)
print("Method 1: pd.DataFrame.from_records()")
print(df1)
print()

# Method 2: Passing data directly to pd.DataFrame()
df2 = pd.DataFrame(simulated_response)
print("Method 2: pd.DataFrame()")
print(df2)
print("\nBoth methods produce the same result!\n")

# Real-world example structure
print("=" * 60)
print("COMPLETE API TO DATAFRAME PIPELINE")
print("=" * 60)
print("""
import requests
import pandas as pd

def fetch_and_process_data(api_url):
    '''
    Fetch data from API and convert to pandas DataFrame
    
    Args:
        api_url (str): URL of the API endpoint
    
    Returns:
        pd.DataFrame: Processed data
    '''
    try:
        # Make GET request
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse JSON response
        data = response.json()
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return None

# Usage
# df = fetch_and_process_data("https://api.example.com/data")
""")

# =============================================================================
# MLOps: MODEL VERSIONING
# =============================================================================

print("=" * 60)
print("MLOps: MODEL VERSIONING FOR TRACKING AND REPRODUCIBILITY")
print("=" * 60)

print("""
MODEL VERSIONING means ASSIGNING A UNIQUE IDENTIFIER to each model update

Why is model versioning critical?
1. Tracking: Know which model version is deployed in production
2. Reproducibility: Recreate exact model results
3. Rollback: Return to previous version if new model underperforms
4. Comparison: Compare performance across different versions
5. Compliance: Maintain audit trail for regulated industries

Common versioning strategies:

1. Semantic Versioning (MAJOR.MINOR.PATCH)
   - MAJOR: Breaking changes (e.g., different features)
   - MINOR: New features, backward compatible
   - PATCH: Bug fixes
   Example: v2.1.3

2. Timestamp-based
   - Format: YYYYMMDD-HHMMSS
   Example: 20240315-143022

3. Git commit hash
   - Links model to exact code version
   Example: a3f5c8d

4. Sequential numbering
   - Simple incrementing numbers
   Example: model_001, model_002, model_003
""")

# Example: Simple model versioning system
print("\nExample: Model Version Tracking\n")

class ModelVersion:
    """
    Simple model versioning system
    """
    def __init__(self, major=1, minor=0, patch=0):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.metadata = {}
    
    def __str__(self):
        return f"v{self.major}.{self.minor}.{self.patch}"
    
    def increment_patch(self):
        """Bug fix or minor update"""
        self.patch += 1
    
    def increment_minor(self):
        """New feature, backward compatible"""
        self.minor += 1
        self.patch = 0
    
    def increment_major(self):
        """Breaking change"""
        self.major += 1
        self.minor = 0
        self.patch = 0
    
    def add_metadata(self, key, value):
        """Add metadata like accuracy, training date, etc."""
        self.metadata[key] = value

# Usage example
model_v1 = ModelVersion(1, 0, 0)
model_v1.add_metadata("accuracy", 0.85)
model_v1.add_metadata("training_date", "2024-03-15")
model_v1.add_metadata("dataset_size", 10000)

print(f"Model version: {model_v1}")
print(f"Metadata: {model_v1.metadata}\n")

# After bug fix
model_v1.increment_patch()
print(f"After bug fix: {model_v1}\n")

# After adding new feature
model_v2 = ModelVersion(1, 0, 1)
model_v2.increment_minor()
print(f"After new feature: {model_v2}\n")

# =============================================================================
# AI SYSTEM PROTOTYPE vs PRODUCTION
# =============================================================================

print("=" * 60)
print("AI SYSTEM PROTOTYPE vs PRODUCTION DEPLOYMENT")
print("=" * 60)

print("""
AI SYSTEM PROTOTYPE typically includes:
✓ Data pre-processing pipelines
✓ Model training and selection
✓ Model evaluation and metrics
✓ Basic inference functionality
✓ Performance benchmarking

AI SYSTEM PROTOTYPE does NOT typically include:
✗ Long-term system maintenance scheduling (PRODUCTION CONCERN)
✗ 24/7 monitoring and alerting
✗ Automated model retraining pipelines
✗ Load balancing and scaling
✗ Disaster recovery plans
✗ Security audits and compliance checks

Why the distinction?
- Prototypes focus on PROOF OF CONCEPT
- Production systems focus on RELIABILITY, SCALABILITY, and MAINTENANCE
- System maintenance scheduling is part of MLOps/DevOps, not prototyping
""")

# Example prototype structure
print("\nExample AI Prototype Structure:\n")
print("""
project/
├── data/
│   ├── raw/                  # Original data
│   └── processed/            # Cleaned data
├── notebooks/
│   ├── 01_exploration.ipynb  # Data analysis
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── preprocessing.py      # Data cleaning functions
│   ├── model.py             # Model definition
│   └── evaluation.py        # Metrics and validation
├── models/
│   └── best_model.pkl       # Saved model
├── requirements.txt         # Dependencies
└── README.md               # Documentation

This is sufficient for a PROTOTYPE to demonstrate feasibility.
""")

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. MinMaxScaler - Normalize features to [0, 1] range
   → Always fit on training data only!

2. OneHotEncoder - Convert categorical features to binary columns
   → Use sparse_output=False for regular arrays

3. Label Encoding - Find INDEX of category in unique categories list
   → Maps categories to integers (0, 1, 2, ...)

4. Llama Inference - INPUT PROMPT STRUCTURE is most critical
   → Use proper tokens and system messages

5. LLM Fine-tuning - CONTINUE TRAINING on specialized dataset
   → Adapts model to specific domain

6. API Data Fetching - requests.get() + .json()
   → Use pd.DataFrame() or pd.DataFrame.from_records()

7. Model Versioning - UNIQUE IDENTIFIER for each model update
   → Essential for tracking and reproducibility

8. Prototype vs Production - Prototypes exclude MAINTENANCE SCHEDULING
   → Production requires ongoing MLOps infrastructure
""")
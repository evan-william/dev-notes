"""
PyTorch & NumPy Fundamentals
============================
This file covers essential PyTorch and NumPy operations for deep learning.
"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# =============================================================================
# CREATING TENSORS
# =============================================================================

print("=" * 60)
print("CREATING TENSORS FROM DIFFERENT SOURCES")
print("=" * 60)

# 1. Creating a tensor from a Python list
# Use torch.tensor() to convert Python lists to tensors
python_list = [1, 2, 3, 4, 5]
tensor_from_list = torch.tensor(python_list)
print(f"Python list: {python_list}")
print(f"Tensor from list: {tensor_from_list}")
print(f"Type: {type(tensor_from_list)}\n")

# 2D list example
list_2d = [[1, 2, 3], [4, 5, 6]]
tensor_2d = torch.tensor(list_2d)
print(f"2D tensor:\n{tensor_2d}")
print(f"Shape: {tensor_2d.shape}\n")

# 2. Creating a tensor from a NumPy array
# Use torch.from_numpy() - this is the standard method
numpy_array = np.array([10, 20, 30, 40, 50])
tensor_from_numpy = torch.from_numpy(numpy_array)
print(f"NumPy array: {numpy_array}")
print(f"Tensor from NumPy: {tensor_from_numpy}")
print(f"Type: {type(tensor_from_numpy)}\n")

# Important: torch.from_numpy() creates a tensor that shares memory with the NumPy array
# Modifying one will modify the other
numpy_array[0] = 999
print(f"After modifying NumPy array:")
print(f"NumPy array: {numpy_array}")
print(f"Tensor: {tensor_from_numpy}")
print("Notice both changed!\n")

# To avoid shared memory, use .clone()
numpy_array2 = np.array([1, 2, 3, 4, 5])
tensor_independent = torch.from_numpy(numpy_array2).clone()
numpy_array2[0] = 100
print(f"With .clone():")
print(f"NumPy array: {numpy_array2}")
print(f"Tensor: {tensor_independent}")
print("They're independent!\n")

# =============================================================================
# NEURAL NETWORK LAYERS
# =============================================================================

print("=" * 60)
print("CREATING NEURAL NETWORK LAYERS")
print("=" * 60)

# Creating a fully-connected (Linear) layer
# nn.Linear(in_features, out_features)
# in_features: size of input
# out_features: size of output

# Example: Transform 10 features to 5 features
layer1 = nn.Linear(in_features=10, out_features=5)
print(f"Layer 1: {layer1}")
print(f"Weight shape: {layer1.weight.shape}")  # (out_features, in_features)
print(f"Bias shape: {layer1.bias.shape}\n")    # (out_features,)

# Example: Create a sample input and pass through layer
sample_input = torch.randn(3, 10)  # 3 samples, 10 features each
output = layer1(sample_input)
print(f"Input shape: {sample_input.shape}")
print(f"Output shape: {output.shape}\n")

# Building a simple neural network architecture
class SimpleNetwork(nn.Module):
    def __init__(self):
        super(SimpleNetwork, self).__init__()
        self.layer1 = nn.Linear(in_features=20, out_features=10)
        self.layer2 = nn.Linear(in_features=10, out_features=5)
        self.layer3 = nn.Linear(in_features=5, out_features=1)
    
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x

model = SimpleNetwork()
print(f"Simple Network Architecture:\n{model}\n")

# =============================================================================
# ACTIVATION FUNCTIONS
# =============================================================================

print("=" * 60)
print("ACTIVATION FUNCTIONS FOR MULTI-CLASS CLASSIFICATION")
print("=" * 60)

# For multi-class classification, use Softmax to convert outputs to probabilities
# nn.Softmax(dim=1) - dim=1 means apply softmax across columns (classes)

# Example: 3 samples, 4 classes
logits = torch.randn(3, 4)  # Raw network outputs
print(f"Raw logits (before softmax):\n{logits}\n")

softmax = nn.Softmax(dim=1)
probabilities = softmax(logits)
print(f"Probabilities (after softmax):\n{probabilities}\n")

# Check that probabilities sum to 1 for each sample
print(f"Sum of probabilities per sample:\n{probabilities.sum(dim=1)}\n")

# Complete multi-class classification network
class MultiClassNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(MultiClassNetwork, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_size, num_classes)
        self.softmax = nn.Softmax(dim=1)
    
    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.softmax(x)
        return x

# Create a model for classifying into 3 classes
classifier = MultiClassNetwork(input_size=10, hidden_size=8, num_classes=3)
sample_data = torch.randn(5, 10)  # 5 samples, 10 features
predictions = classifier(sample_data)
print(f"Multi-class predictions (probabilities):\n{predictions}\n")

# =============================================================================
# ONE-HOT ENCODING AND ARGMAX
# =============================================================================

print("=" * 60)
print("CONVERTING ONE-HOT TO CLASS INDICES")
print("=" * 60)

# One-hot encoded labels: each row has a 1 in the position of the true class
one_hot_labels = torch.tensor([
    [1, 0, 0],  # Class 0
    [0, 1, 0],  # Class 1
    [0, 0, 1],  # Class 2
    [1, 0, 0],  # Class 0
    [0, 1, 0]   # Class 1
])

print(f"One-hot encoded labels:\n{one_hot_labels}\n")

# Convert to class indices using torch.argmax()
# dim=1 means find the max along columns (across classes)
class_indices = torch.argmax(one_hot_labels, dim=1)
print(f"Class indices: {class_indices}\n")

# Why do we need this?
# nn.CrossEntropyLoss expects class indices, NOT one-hot encoded labels
print("nn.CrossEntropyLoss requires class indices as targets!")
print("So if you have one-hot encoded labels, use torch.argmax() first.\n")

# Example with loss calculation
predictions_logits = torch.randn(5, 3)  # 5 samples, 3 classes
targets = class_indices  # Use class indices

criterion = nn.CrossEntropyLoss()
loss = criterion(predictions_logits, targets)
print(f"CrossEntropyLoss value: {loss.item():.4f}\n")

# =============================================================================
# OPTIMIZERS
# =============================================================================

print("=" * 60)
print("INITIALIZING OPTIMIZERS")
print("=" * 60)

# Adam optimizer is one of the most popular optimizers
# It adapts the learning rate during training

# Create a simple model
simple_model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 2)
)

# Initialize Adam optimizer
# You MUST pass the model's parameters and a learning rate
learning_rate = 0.001
optimizer = optim.Adam(simple_model.parameters(), lr=learning_rate)

print(f"Optimizer: {optimizer}\n")

# How to use the optimizer in a training loop
print("Training loop structure:")
print("""
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    
    # Backward pass
    optimizer.zero_grad()  # Clear old gradients
    loss.backward()        # Compute new gradients
    optimizer.step()       # Update weights
""")

# Complete training example
print("\nComplete training example:\n")

# Generate dummy data
X_train = torch.randn(100, 10)  # 100 samples, 10 features
y_train = torch.randint(0, 2, (100,))  # 100 binary labels

# Model, loss, optimizer
model = nn.Sequential(
    nn.Linear(10, 8),
    nn.ReLU(),
    nn.Linear(8, 2)
)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
num_epochs = 5
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")

# =============================================================================
# TORCHMETRICS FOR EVALUATION
# =============================================================================

print("\n" + "=" * 60)
print("CALCULATING ACCURACY WITH TORCHMETRICS")
print("=" * 60)

try:
    import torchmetrics
    
    # For binary classification
    # Initialize with task="binary"
    accuracy_metric = torchmetrics.Accuracy(task="binary")
    
    # Example predictions and targets
    preds = torch.tensor([0, 1, 1, 0, 1])
    targets = torch.tensor([0, 1, 0, 0, 1])
    
    accuracy = accuracy_metric(preds, targets)
    print(f"Binary Classification Accuracy: {accuracy:.4f}\n")
    
    # For multi-class classification
    accuracy_multiclass = torchmetrics.Accuracy(task="multiclass", num_classes=3)
    
    preds_mc = torch.tensor([0, 2, 1, 0, 2])
    targets_mc = torch.tensor([0, 1, 1, 0, 2])
    
    accuracy_mc = accuracy_multiclass(preds_mc, targets_mc)
    print(f"Multi-class Classification Accuracy: {accuracy_mc:.4f}\n")
    
except ImportError:
    print("torchmetrics not installed. Install with: pip install torchmetrics\n")
    print("Alternative: Calculate accuracy manually")
    preds = torch.tensor([0, 1, 1, 0, 1])
    targets = torch.tensor([0, 1, 0, 0, 1])
    accuracy = (preds == targets).float().mean()
    print(f"Manual Binary Accuracy: {accuracy:.4f}\n")

print("=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. torch.tensor() - Create tensors from Python lists
2. torch.from_numpy() - Create tensors from NumPy arrays (shares memory!)
3. nn.Linear(in_features, out_features) - Fully connected layer
4. nn.Softmax(dim=1) - Convert logits to probabilities for multi-class
5. torch.argmax(tensor, dim=1) - Convert one-hot to class indices
6. optim.Adam(model.parameters(), lr=...) - Initialize Adam optimizer
7. torchmetrics.Accuracy(task="binary") - Calculate binary accuracy
""")
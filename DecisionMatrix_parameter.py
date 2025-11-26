# Importing necessary libraries
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
import numpy as np

# Simulated predictions and actual values
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0, 1, 0])

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)

# Extracting values
TP = cm[1, 1]
FP = cm[0, 1]
FN = cm[1, 0]
TN = cm[0, 0]

print("Confusion Matrix:")
print(cm)
print("\nFalse Positives:", FP)
print("False Negatives:", FN)

# Calculating precision, recall, and F1-score
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("\nPrecision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
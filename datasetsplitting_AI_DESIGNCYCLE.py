from sklearn.model_selection import train_test_split
import pandas as pd

# Load your dataset (replace with your file path or data source)
data = pd.read_csv('D:\PUNIT_NAMDEO\FACIAL_LAB\PythonSourceCode\collected_data.csv')  # Replace with your actual dataset

# Separate features and target (assumes the last column is the target)
X = data.iloc[:, :-1]  # all rows, all columns except the last
y = data.iloc[:, -1]   # all rows, just the last column

# Perform 80-20 train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Output the sizes of the splits
print("Training set size:", X_train.shape)
print("Test set size:", X_test.shape)

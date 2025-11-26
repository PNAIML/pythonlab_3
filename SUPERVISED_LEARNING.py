# Supervised Learning Example: Logistic Regression Classifier

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset (age, education_years, income: 0 = <=50K, 1 = >50K)
data = [
    [25, 10, 0],
    [45, 16, 1],
    [35, 14, 1],
    [22, 9, 0],
    [60, 15, 1],
    [33, 11, 0]
]



# Splitting features and target
X = [row[:2] for row in data]  # Features: age, education_years
y = [row[2] for row in data]  # Target: income

# Split into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6)

# Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test data
predictions = model.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, predictions)
print("Predictions:", predictions)
print("Actual:", y_test)
print("Accuracy:", accuracy)

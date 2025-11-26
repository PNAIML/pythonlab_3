# Unsupervised Learning Example: K-Means Clustering

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data: [Height (cm), Weight (kg)]
data = [
    [160, 60],
    [155, 85],
    [170, 65],
    [180, 85],
    [175, 80],
    [185, 90],
    [150, 50],
    [165, 70]
]

# Create a KMeans clustering model with 2 clusters
model = KMeans(n_clusters=2, random_state=42)
model.fit(data)

# Get cluster predictions
labels = model.labels_

# Print results
for i, point in enumerate(data):
    print(f"Data point {point} belongs to cluster {labels[i]}")

# Plotting the clusters
x = [point[0] for point in data]
y = [point[1] for point in data]

plt.scatter(x, y, c=labels, cmap='viridis')
plt.title("K-Means Clustering")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.show()
# Here's a simple Python program that demonstrates unsupervised learning using the popular scikit-learn library. We’ll use the K-Means Clustering algorithm to group data points into clusters without any labeled output.
#What this does:
#- This is unsupervised learning because the algorithm doesn’t know which group each data point belongs to beforehand.
#- It uses K-Means, which tries to partition the data into K distinct, non-overlapping subgroups (clusters).
#- The model learns patterns based entirely on the structure of the input data.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate random data for demonstration
data, _ = make_blobs(n_samples=300, centers=4, random_state=42)

# Apply k-means algorithm
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(data)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Visualize the clustered data
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', alpha=0.5, edgecolors='k')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Cluster Centers')
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

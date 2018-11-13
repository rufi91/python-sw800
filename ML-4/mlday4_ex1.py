"""
Prepare an ML model using KMeans algorithm to cluster some sample input
generated using make_blob function. Plot the clusters.
"""

from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60)
plt.scatter(X[:,0], X[:,1], s=20)
plt.title("generated data")
plt.show()

kmeans= KMeans(n_clusters=4)
kmeans.fit(X)
plt.scatter(X[:,0], X[:,1], s=20, c=y_true, cmap='viridis')
plt.title("KMeans Clustered Data")
plt.show()

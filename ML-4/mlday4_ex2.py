"""Prepare an ML model using KMeans algorithm to cluster some sample input
generated using make_moon function. Plot the clusters. Also plot the same
points by clustering it with Spectral Clustering Model.
"""

from sklearn.datasets import make_moons
from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt

X, y_true = make_moons(n_samples=300,noise=0.05)

plt.scatter(X[:,0], X[:,1], s=20)
plt.title("generated data")
plt.show()

spCluster= SpectralClustering(n_clusters=3, n_init=20)
spCluster.fit_predict(X)
plt.scatter(X[:,0], X[:,1], s=20, c=y_true, cmap='viridis')
plt.title("KMeans Clustered Data")
plt.show()


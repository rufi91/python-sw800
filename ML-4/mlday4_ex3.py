"""Try clustering with some suitable datasets in the link
http://cs.joensuu.fi/sipu/datasets/
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('datakmeans.txt', delimiter='  ')
X=data.as_matrix()
print X.shape

plt.scatter(X[:,0], X[:,1], s=20)
plt.title("generated data")
plt.show()

kmeans= KMeans(n_clusters=19)
model=kmeans.fit(X)

plt.scatter(X[:,0], X[:,1], s=20, c=model.labels_.astype(float))
plt.title("KMeans Clustering Data")
plt.show()



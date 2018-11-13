"""Try clustering with some suitable datasets in the link
http://cs.joensuu.fi/sipu/datasets/ #D
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 
import pandas as pd

data=pd.read_csv('3ddatakmeans.txt', delimiter='\s+')
X=data.as_matrix()
print X.shape

x1=X[:,0]
x2=X[:,1]
x3=X[:,2]

kmeans= KMeans(n_clusters=11)
kmeans.fit(X)
model=kmeans.predict(X)
fig=plt.figure()
ax=plt.axes(projection="3d")
ax.scatter3D(x1,x2,x3,c=model,cmap="viridis")

#plt.scatter(X[:,0], X[:,1], s=20, c=model.labels_.astype(float))
plt.title("KMeans Clustering Data")
plt.show()



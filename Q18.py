import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering

X, y = make_blobs(
    n_samples=100,
    centers=3,
    random_state=42
)

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
k_labels = kmeans.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=k_labels)
plt.title("K-Means Clustering")
plt.show()

# Hierarchical Clustering
hc = AgglomerativeClustering(n_clusters=3)
h_labels = hc.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=h_labels)
plt.title("Hierarchical Clustering")
plt.show()
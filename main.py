import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.metrics import pairwise_distances_argmin

data = pd.read_csv('dataset/Mall_Customers.csv')
# print(data.head(10))

data = data.iloc[:, [3, 4]].values
# print(data.head(10))

# plt.scatter(data[:, 0], data[:, 1], s=10, c='blue')
# plt.show()

model = DBSCAN(eps=1, min_samples=5)

y_pred = model.fit_predict(data)

print(y_pred)
print(np.unique(y_pred))


def find_clusters(x, clusters, seed=2):
    rng = np.random.RandomState(seed)
    i = rng.permutation(x.shape[0])[:clusters]
    centers = x[i]

    while True:
        labels = pairwise_distances_argmin(x, centers)

        new_centers = np.array([x[labels == i].mean(0) for i in range(clusters)])

        if np.all(centers == new_centers):
            break
        centers = new_centers

    return centers, labels


centers, labels = find_clusters(data, 4)
plt.scatter(data[:, 0], data[:, 1], c=y_pred, s=50, cmap='viridis')
# plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()

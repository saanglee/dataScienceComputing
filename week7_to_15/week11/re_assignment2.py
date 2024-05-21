import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.colors as mcolors
# %matplotlib inline

# data is ./dataset.csv


class Kmeans:

    def __init__(self, data, k=3, max_iter = None, threshold=1e-6):
        self.data = data
        self.k = k
        self.max_iter = max_iter
        self.threshold = threshold
        self.colors = list(mcolors.TABLEAU_COLORS)
        self.centroids = np.array(self.data[['x', 'y']].head(self.k))

    def show(self, clusters=None):
        ### Edit Here ###
        # Show data points
        plt.figure(figsize=(10, 6))
        if clusters is not None:
            for i in range(self.k):
                plt.scatter(self.data.loc[clusters == i, 'x'], self.data.loc[clusters == i, 'y'], color=self.colors[i], label=f'Cluster {i}')
            plt.scatter(self.centroids[:, 0], self.centroids[:, 1], color='red', s=100, marker='x', label='Centroids')
            plt.legend()
        else:
            plt.scatter(self.data['x'], self.data['y'], color='black')
            plt.scatter(self.centroids[:, 0], self.centroids[:, 1], color='red', s=100, marker='x')
        plt.title('K-means Clustering')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()


    def distance(self, d1, d2):
        # Calculate the Euclidean distance
        return np.linalg.norm(d1 - d2, axis=1)

    def assign_centroid(self):
        # Assign each data point to the nearest centroid
        distances = np.zeros((len(self.data), self.k))
        for i, centroid in enumerate(self.centroids):
            distances[:, i] = self.distance(centroid, self.data[['x', 'y']].values)
        return np.argmin(distances, axis=1)

    def update(self):
        # Update centroids
        clusters = self.assign_centroid()
        for i in range(self.k):
            self.centroids[i] = np.mean(self.data.loc[clusters == i, ['x', 'y']], axis=0)

if __name__ == '__main__':
    # Load dataset
    dataset = pd.read_csv('./dataset.csv')
    
    # Initialize Kmeans
    # kmeans = Kmeans(dataset)
    initial_centroids = [(5, 25), (30, 35), (35, 10)]
    kmeans = Kmeans(dataset, initial_centroids=initial_centroids)
    
    # Show initial state
    kmeans.show()
    
    # Update centroids and show clustering
    for _ in range(kmeans.max_iter):  # You can adjust the number of iterations
        clusters = kmeans.assign_centroid()
        kmeans.update()
        kmeans.show(clusters=clusters)
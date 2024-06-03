import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.colors as mcolors
import random

class Kmeans:

    def __init__(self, data, k=3, max_iter=100, threshold=1e-6):
        self.data = data
        self.k = k
        self.max_iter = max_iter
        self.threshold = threshold
        self.colors = list(mcolors.TABLEAU_COLORS)
        self.centroids = self.initialize_centroids()
        self.labels = np.zeros(len(data))
      
    def initialize_centroids(self):
        # Randomly select k data points as initial centroids
        indices = random.sample(range(len(self.data)), self.k)
        print('initial indeces: ', indices)
        print('initial centroids: ', self.data[indices])
        return self.data[indices]

    def show(self):
        plt.figure(figsize=(8, 6))
        for i in range(self.k):
            points = self.data[self.labels == i]
            plt.scatter(points[:, 0], points[:, 1], s=30, color=self.colors[i], label=f'Cluster {i+1}')
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s=300, c='black', marker='X')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

    def distance(self, d1, d2):
        return np.sqrt(np.sum((d1 - d2) ** 2))

    def assign_to_centroid(self):
        for i, point in enumerate(self.data):
            distances = [self.distance(point, centroid) for centroid in self.centroids]
            self.labels[i] = np.argmin(distances)

    def update_centroids(self):
        new_centroids = np.zeros((self.k, self.data.shape[1]))
        for i in range(self.k):
            points = self.data[self.labels == i]
            if len(points) > 0:
                new_centroids[i] = np.mean(points, axis=0)
        return new_centroids

    def fit(self):
        for _ in range(self.max_iter):
            self.assign_to_centroid()
            new_centroids = self.update_centroids()
            if np.all(np.abs(self.centroids - new_centroids) < self.threshold):
                break
            self.centroids = new_centroids

# Load the data from the CSV file
# file_path = '/mnt/data/dataset.csv'
# data = pd.read_csv(file_path)

data = pd.read_csv('dataset.csv')
data_points = data[['x', 'y']].values

kmeans = Kmeans(data_points, k=3)
kmeans.fit()
kmeans.show()

# data is dataset.csv
# data = pd.read_csv('dataset.csv')

# if __name__ == '__main__':
#     kmeans = Kmeans(data)
#     kmeans.show() # cluster 부여 전 데이터 시각화

#     kmeans.update()
#     kmeans.show() # cluster 부여 후 cluster별 색상 부여 및 데이터와 centroid 시각화

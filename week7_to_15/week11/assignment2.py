import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.colors as mcolors
# %matplotlib inline

# data is dataset.csv

""" dataset
ID,x,y
0,24.412,32.932
1,35.19,12.189
2,26.288,41.718
3,0.376,15.506
4,26.116,3.963
5,25.893,31.515
"""

class Kmeans:

    def __init__(self, data, k=3, max_iter = None, threshold=1e-6):
        self.data = data
        self.k = k
        self.max_iter = max_iter
        self.threshold = threshold
        self.colors = list(mcolors.TABLEAU_COLORS)
        self.centroids = np.array(self.data[['x', 'y']].head(self.k))


    def show(self): # Show data points
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data['x'], self.data['y'], color='black')
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], color='red', s=100, marker='x')
        plt.show()

    def distance(self, d1, d2): # Calculate the distance
        return np.sqrt(np.sum((d1 - d2) ** 2))
    

    def assign_centroid(self): # Assign each data point to nearest centroid
        clusters = [[] for _ in range(self.k)]
        for d in self.data:
            min_dist = float('inf')
            cluster_idx = -1
            for i in range(self.k):
                dist = self.distance(d, self.centroids[i])
                if dist < min_dist:
                    min_dist = dist
                    cluster_idx = i
            clusters[cluster_idx].append(d)
        return clusters




    def update(self): # Update centroids
        for i in range(self.k):
            cluster = np.array(self.assign_centroid()[i])
            new_centroid = np.mean(cluster, axis=0)
            self.centroids[i] = new_centroid
        
# data is dataset.csv
data = pd.read_csv('dataset.csv')

if __name__ == '__main__':
    kmeans = Kmeans(data)
    kmeans.show() # cluster 부여 전 데이터 시각화

    kmeans.update()
    kmeans.show() # cluster 부여 후 cluster별 색상 부여 및 데이터와 centroid 시각화
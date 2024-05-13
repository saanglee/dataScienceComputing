
import numpy as np

class CoordArray:
    def __init__(self, N):
        np.random.seed(0)
        self.n = N
        self.array = np.random.randint(-10, 11, (N, 2))
        self.col_avg = None
        self.row_avg = None

    def mean(self, axis):
        # 각 행별 평균, 열별 평균을 구하는 함수
        if axis == 0:
            self.col_avg = np.mean(self.array, axis=0)
            return self.col_avg
        elif axis == 1:
            self.row_avg = np.mean(self.array, axis=1)
            return self.row_avg
        else:
            return None

    def sort(self):
        # 원점(0,0)과의 거리를 기준으로 좌표행렬을 내림차순 정렬하는 함수
        distances = np.linalg.norm(self.array, axis=1)
        sorted_indices = np.argsort(distances)[::-1]  # Sort indices in descending order
        self.array = self.array[sorted_indices]

    def distance(self, x:int, y:int):
        # 새로운 좌표 x, y를 입력받으면 좌표 행렬에서 각 좌표와 거리를 구하고, 
        # 가장 먼 좌표와의 거리를 반환하는 함수
        point = np.array([x, y])
        distances = np.linalg.norm(self.array - point, axis=1)
        max_distance = np.max(distances)
        return round(max_distance, 2)


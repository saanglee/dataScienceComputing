import numpy as np

np.random.seed(0)
random_arr = np.random.rand(5)
print(random_arr) # array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ])

n = 5
arr = np.random.randint(-10, 11, (n, 2)) # from -10 to 10, n*2 arr

col_avg = np.mean(arr, axis=0) # column mean
row_avg = np.mean(arr, axis=1)


arr = np.array([[1, 2], [-3, 4], [5, 6]])
distances = np.linalg.norm(arr, axis=1) # the distance between each coordinate and the origin (0, 0)

# np.argsort(array) 배열을 정렬했을 때의 인덱스를 반환
sorted_indices = np.argsort(distances) 

# descending sort
sorted_indices_desc = sorted_indices[::-1]

# 정렬된 인덱스로 배열을 정렬
arr = arr[sorted_indeces_desc]



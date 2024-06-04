import numpy as np

np.random.seed(0)
random_arr = np.random.rand(5)
print(random_arr) 

n = 5
arr = np.random.randint(-10, 11, (n, 2))

col_avg = np.mean(arr, axis=0) # col
row_avg = np.mean(arr, axis=1)


arr = np.array([[1, 2], [-3, 4], [5, 6]])
distances = np.linalg.norm(arr, axis=1)

sorted_indices = np.argsort(distances) # return 배열 정렬시 index

sorted_indices_desc = sorted_indices[::-1] 

# 정렬된 인덱스로 배열을 정렬
# arr = arr[sorted_indeces_desc]

np.arange(0, 3, 0.5) # array([0. , 0.5, 1. , 1.5, 2. , 2.5])
np.linspace(0, 1, 5) # [0.  , 0.25, 0.5 , 0.75, 1.  ]
np.zeros((2, 3))

arr = np.ragne(6) # 0 ~ 5
arr.resahpe((2,3))
np.sum(arr)
np.transpose(arr)

condition = arr % 2 == 0
indices = np.where(condition)




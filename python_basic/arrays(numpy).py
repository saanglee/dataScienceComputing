import numpy as np

# CREATING A 1D ARRAY
arr_1d = np.array([1,2,3,4,5])
print(arr_1d)

arr_2d = np.array([[1,2,3],[4,5,6]])

print('Shape: ', arr_2d.shape)
print('Number of dimensions: ', arr_2d.ndim)
print('Size: ', arr_2d.size)
print('Data type: ', arr_2d.dtype)
print('Size of each element(in bytes):', arr_2d.itemsize)

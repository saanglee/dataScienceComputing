import numpy as np

# Create a 1D array
a = np.array([1, 2, 3, 4, 5])
# print(a)

# Create a 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)

# Create a 3D array
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(c)

c2 = np.array([(1,2,3), ('a', 'b', 'c'), ('가', '나', '다')])
# print(c2)

c3 = np.array([1, 2, 3], dtype=complex)
# print(c3)

# Create an array of zeros
d = np.zeros((2, 3))
# print(d)

# Create an array of ones
e = np.ones((6, 3))
# print(e)

# Create an array of full
f = np.full((2, 5), 99, dtype=float)
# print(f)

# like 
g = np.zeros_like(f)
g2 = np.ones_like(f)
g3 = np.full_like(f, 777)

# print(g)
# print(g2)
# print(g3)

# Create an array of random values
h = np.random.random((3, 2))

# Create an array of evenly spaced values
i = np.arange(10)
i2 = np.arange(2, 10, 2) # start, end, step
i3 = np.arange(12).reshape(3, 4)
print(i)
print(i2)
print(i3)

# linspace
j = np.linspace(1, 5, 5) # start, end, num
j2 = np.linspace(1, 5, 5, endpoint=False) # start, end, num, endpoint
j3 = np.linspace(1, 5, 5, retstep=True) # start, end, num, retstep
print(j)
print(j2)
print(j3)

# logspace
k = np.logspace(1, 5, 5) # start, end, num

# random
l = np.random.rand(2, 3) # 0~1
l2 = np.random.randn(2, 3) # 정규분포
l3 = np.random.randint(1, 100, (2, 3)) # start, end, size 지정된 수 범위에서 균등하게 추출
l4 = np.random.normal(0, 1, (2, 3)) # 평균(M), 표준편차(SD), size

# 난수 생성
np.random.seed(0)

# 덧셈, 뺄셈, 곱셈, 나눗셈
m = np.array([1, 2, 3])
m2 = np.array([4, 5, 6])
m3 = m + m2
m4 = m - m2
m5 = m * m2
m6 = m / m2

# 슬라이싱과 인덱싱 - 동일




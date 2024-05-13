"""
Recursion and Iteration - Dynamic Programming

Dynamic Programming
- 복잡한 문제를 간단한 여러개의 문제로 나누어 푸는 방법

1. 입력 크기가 작은 부분 먼저 모두 해결
2 ...

-> 어떤 문제가 여러 단계로 반복되는 부분 문제로 이루어질 때,
각 단계의 부문 문제의 답을 기반으로 전체 답을 구하는 방법

- 분할 정복 알고리즘과 동적 계획 알고리즘의 차이
  - 분할 정복 알고리즘은 부분문제의 해를 중복 사용하지 않음! (disjoint하다)
  - 동적 계획: 부분문제들 사이에 의존적 관계가 있음

"""

### 피보나치 ###

def fibo(n):
  i = 1
  bunny, rabby = 1, 0
  while i < n:
    i = i + 1
    temp = bunny
    bunny = rabby
    rabby = temp + rabby
  return bunny + rabby

def fibo2(n):
  bunny, rabby = 1, 0
  for _ in range(2, n+1):
    bunny, rabby = rabby, bunny+rabby
  return bunny + rabby

def fibseq(n):
  fibs = [0, 1]
  for k in range(2, n+2):
    fibs.append(fibs[k-1]+fibs[k-2])
  return fibs


### ⭐️ 파스칼 삼각형 (시험) ###

def comb_pascal(n, r):
  matrix = [[]] * (n - r + 1)
  matrix[0] = [1] * (r + 1)
  for i in range(1, n-r+1):
    matrix[i] = [1]
  for i in range(1, n-r+1):
    for j in range (1, r+1):
      newvalue = matrix[i][j-1] + matrix[i-1][j]
      matrix[i].append(newvalue)
    return matrix[n-r][r]



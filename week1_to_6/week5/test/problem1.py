def pathFinder(m, n):
    memo = [[0] * n for _ in range(m)]  
    if obstacleGrid[0][0] == 0:  
        memo[0][0] = 1

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 0:  
                if i > 0:
                    memo[i][j] += memo[i - 1][j]  
                if j > 0:
                    memo[i][j] += memo[i][j - 1]  
    return memo[-1][-1]  


#### Do not edit here ####
import random

random.seed(500)

print("격자의 크기를 입력하세요 (m n): ", end="")
m, n = map(int, input().split())

obstacle_rate = 0.3 
obstacleGrid = [[0 if random.random() >= obstacle_rate else 1 for _ in range(n)] for _ in range(m)]
obstacleGrid[0][0] = 0 
obstacleGrid[m-1][n-1] = 0

result = pathFinder(n, m)
print(f'경로의 개수는 {result}개 입니다.')
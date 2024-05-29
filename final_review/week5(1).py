# def pathFinder(m, n):
#     memo = [[0] * n for _ in range(m)]  
#     if obstacleGrid[0][0] == 0:  
#         memo[0][0] = 1

#     for i in range(m):
#         for j in range(n):
#             if obstacleGrid[i][j] == 0:  
#                 if i > 0:
#                     memo[i][j] += memo[i - 1][j]  
#                 if j > 0:
#                     memo[i][j] += memo[i][j - 1]  
#     return memo[-1][-1]  


# #### Do not edit here ####
# import random

# random.seed(500)

# print("격자의 크기를 입력하세요 (m n): ", end="")
# m, n = map(int, input().split())

# obstacle_rate = 0.3 
# obstacleGrid = [[0 if random.random() >= obstacle_rate else 1 for _ in range(n)] for _ in range(m)]
# obstacleGrid[0][0] = 0 
# obstacleGrid[m-1][n-1] = 0

# result = pathFinder(n, m)
# print(f'경로의 개수는 {result}개 입니다.')




### DP 문제 ###

def solution(m, n, puddles):
    div = 1000000007
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for pd in puddles:
        dp[pd[0]][pd[1]] = -1
    dp[1][1] = 1

    def routes(n, m):
        if dp[n][m] > 0:
            return dp[n][m]
        if n < 1 or m < 1 or dp[n][m] == -1:
            return 0
        dp[n][m] = routes(n-1, m)+routes(n, m-1)
        return dp[n][m]

    return routes(n, m) % div


m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))

# https://eijun.tistory.com/179
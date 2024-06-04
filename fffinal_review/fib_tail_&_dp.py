N = int(input())

def fibonacci_tail(n, memo={}):
    count = []
    if n == 0 or n == 1:
        return n
    if not memo.get(n):
        memo[n] = fibonacci_tail(n-2) + fibonacci_tail(n-1)
    return memo[n]

# dp 

def solution(m, n, puddles):
    div = 1000000007 # ?
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
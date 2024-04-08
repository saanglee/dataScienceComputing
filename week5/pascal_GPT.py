
# for i in range (0,2): print(i) # 0, 1
for i in range(1,2): print(i) # 1
for i in range(1,1): print(i) # 0

def combination_DP(n, k):
    # DP 테이블 초기화
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    print('dp: ', dp)
    
    # 파스칼의 삼각형 구성을 위한 기본 케이스 초기화
    for i in range(n+1):
        dp[i][0] = 1  # nC0 = 1
    print('dp: ', dp)

    # 동적 프로그래밍을 이용한 조합의 계산
    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            if j == i:
                dp[i][j] = 1  # nCn = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                
    return dp[n][k]

# 예시: 5개 중에서 3개를 선택하는 방법의 수
print(combination_DP(2, 1))

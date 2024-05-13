
def comb(n,r):
  if not (r == 0 or r == n):
    return comb(n-1, r-1) + comb(n-1, r)
  else:
    return 1
    


n = 2
r = 1


# 파스칼 삼각형을 이용해서 조합을 구하는 함수
def comb_pascal(n, r):
  matrix = [[]] * (n - r + 1 ) 
  matrix[0] = [1] * (r + 1) 

  for i in range (1, n-r+1): # 1부터 n-r+1 까지
    matrix[i] = [1] 
  for i in range(1, n-r+1): 
    for j in range(1, r+1):
      newvalue = matrix[i][j-1] + matrix[i-1][j]
      matrix[i].append(newvalue)
  return matrix[n-r][r]


print(comb_pascal(n, r)) 
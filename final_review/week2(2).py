N = int(input())

def fibonacci_tail(n, memo={}) :
    count = []
    if n == 0 or n==1 :
        return n
    if not memo.get(n) : # memo 에 n 값이 없으면 
        memo[n] = fibonacci_tail(n-2) + fibonacci_tail(n-1) #재귀 후 해시테이블에 저장
        print(f'fibonacci_tail({n}, {n-2}+{n-1}) ')
    return memo[n]

print(fibonacci_tail(N))




# for문 

N = int(input())

def fibonacci(n) :
    if n == 0 :
        return n
    a, b = 0, 1 # 초깃값 두 수 
    for i in range (1, N) :
        temp= a
        a = b
        b= temp+a
    return b

print(fibonacci(N))
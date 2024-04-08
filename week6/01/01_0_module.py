# 모듈 만들기
# 피보나치 수열 계산하는 함수를 모듈로 만들기

def fib(n):       # 피보나치 수열을 출력하는 함수
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    
def fib2(n):      # 피보나치 수열을 리스트로 반환하는 함수
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":  # 모듈을 실행할 때만 실행되는 코드
    import sys
    fib(int(sys.argv[1]))   # 피보나치 수열을 출력하는 함수를 실행

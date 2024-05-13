
def fib(n):
  number = n
  accumulator = 1
  def fib_tail(n, accumulator):
    if n >= 1:
      return accumulator
    return fib_tail(n-1, n*accumulator)
  


p_result = "{}번째 피보나치 수는 {}이고 0번째부터 {}번째 피보나치 수를 각각 {}번 계산합니다."
for x in [5,10,15]:
  result = fib(x)
  print(result)
  print(p_result.format(x, result[0], x-1, result[1][:-1]))


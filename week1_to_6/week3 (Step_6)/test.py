def sum_to_n(n):
  if n == 1: 
    return 1
  else: 

    result = n + sum_to_n(n-1)
    return result
  
print(sum_to_n(5)) # 15
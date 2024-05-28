
def r_sum(n):
    if n ==1:
        return 1
    else:
        return n + r_sum(n-1)


def tail_r_sum(n, total=0):
    if n == 0:
        return total
    else:
        print(n, total)
        return tail_r_sum(n-1, total+n)

# print(r_sum(10))
# print(tail_r_sum(10))


def fib_tail_rec(n, a=0, b=1, count_dict=None):
    if count_dict is None:
        count_dict = {i: 0 for i in range(n+1)}
    count_dict[n] += 1
    if n == 0:
        return a, count_dict
    if n == 1:
        return b, count_dict
    return fib_tail_rec(n-1, b, a+b, count_dict)

def calculate_fib_and_count(N):
    _, count_dict = fib_tail_rec(N)
    fib_number = _ if N < 2 else fib_tail_rec(N-1)[0]
    counts = [count_dict[i] for i in range(N+1)]
    return f"The {N}th Fibonacci number is {fib_number}, and the 0th to {N-1}th Fibonacci numbers are counted {counts} times each."

# Example usage:
N = 5
result = calculate_fib_and_count(N)
print(result)
    
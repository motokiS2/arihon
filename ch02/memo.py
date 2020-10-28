from time import time

n = 35

memo = [0] * n

def fib(n):
    if n <= 1:
        return n
    if memo[n - 1] != 0:
        return memo[n]
    memo[n - 1] = fib(n - 1) + fib(n - 2)
    return memo[n - 1]

start = time()
print(fib(n))
end = time()
print(end - start)
l = int(input())
n = int(input())
x = list(map(int, input().split()))

max_time = max(max(x), l - min(x))

min_time = 0
for xi in x:
    if xi < l / 2:
        min_time = max(min_time, xi)
    else:
        min_time = max(min_time, l - xi)


print(max_time)
print(min_time)
n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            max_a = max(a[i], a[j], a[k])
            if 0 < a[i] + a[j] + a[k] - 2*max_a:
                ans = max(ans, a[i] + a[j] + a[k])

print(ans)
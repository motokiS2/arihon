c1 = 3
c5 = 2
c10 = 1
c50 = 3
c100 = 0
c500 = 2
a = 620

v = [1, 5, 10, 50, 100, 500]
c = [c1, c5, c10, c50, c100, c500]

ans = 0
for i in range(5, -1, -1):
    t = min(a // v[i], c[i])
    a -= t * v[i]
    ans += t

print(ans)
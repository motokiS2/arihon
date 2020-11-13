N = 3
S = [1, 2, 4, 6, 8]
T = [3, 5, 7, 9, 10]

itv = [[0, 0] for _ in range(N)]

for i in range(N):
    itv[i][0] = T[i]
    itv[i][1] = S[i]

itv = sorted(itv)

print(itv)

ans = 0
t = 0
for i in range(N):
    if t < itv[i][1]:
        ans += 1
        t = itv[i][0]

print(ans)
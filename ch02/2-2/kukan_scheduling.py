n = 5
s = [1, 2, 4, 6, 8]
t = [3, 5, 7, 9, 10]

MAX_N = 1e+6

itv = [(0, 0)] * MAX_N

for i in range(n):
    itv[i][0] = t[i]
    itv[i][1] = s[i]


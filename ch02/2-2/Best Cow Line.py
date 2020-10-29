n = 6
s = 'ACDBCB'

a = 0
b = n-1

while a <= b:
    left = False
    for i in range(b - a):
        if s[a + i] < s[b - i]:
            left = True
            break
        elif s[a + i] > s[b - i]:
            left = False
            break

    if left:
        print(s[a], end="")
        a += 1
    else:
        print(s[b], end="")
        b -= 1
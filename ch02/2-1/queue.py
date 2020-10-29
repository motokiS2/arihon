from collections import deque

s = deque([])
print(s)
# push => append()
s.append(1)
s.append(2)
s.append(3)
print(s)

# pop => popleft()
print(s.popleft())
print(s)
print(s.popleft())
print(s)
print(s.popleft())
print(s)
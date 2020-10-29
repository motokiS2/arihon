from collections import deque

n, m = 10, 10
maze = [['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '.', '#'],
        ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
        ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
        ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
        ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
        ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
        ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#']]

INF = 1e+9


def bfs():
    que = deque([])
    sx, sy = -1, -1 # スタートの座標
    gx, gy = -1, -1 # ゴールの座標

    # 右上左下の順
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    # 全ての点をINFで初期化
    d = [[INF] * n for i in range(m)]

    for i in range(n):
        for j in range(m):
            if maze[i][j] == "S":
                sx, sy = j, i
            elif maze[i][j] == "G":
                gx, gy = j, i

    que.append((sx, sy))
    d[sy][sx] = 0

    while len(que):
        x, y = que.popleft()
        if x == gx and y == gy:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < m and 0 <= ny and ny < n and maze[ny][nx] != "#" and d[ny][nx] == INF:
                que.append((nx, ny))
                d[ny][nx] = d[y][x] + 1

    return d[gy][gx]

res = bfs()
print(res)
from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([x, y])
    field[x][y] == 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n and field[nx][ny]==1:
                field[nx][ny] = 0
                q.append([nx, ny])


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        mm, nn = map(int, input().split())
        field[mm][nn] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)


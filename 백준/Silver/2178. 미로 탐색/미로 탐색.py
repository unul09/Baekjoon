import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# .split() 사용은 공백이 포함된 입력의 경우에 사용
miro = [list(map(int, input().rstrip())) for _ in range(n)]

# BFS는 동일한 거리의 노드를 한 번에 탐색하는데, min_path 사용시 방문마다 증가하기 때문에 최소가 아닌 모든 칸을 셈
# 그러므로 방문한 위치에 거리를 저장하는 방법 사용

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()

    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # miro[nx][ny] != 0 조건 설정시 중복된 노드 탐색이 발생
            if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1:
                q.append([nx, ny])
                miro[nx][ny] = miro[x][y]+1

                if nx == n-1 and ny == m-1:
                    return miro[nx][ny]


print(bfs(0, 0))
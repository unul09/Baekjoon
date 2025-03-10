import sys
from collections import deque

# deque(double-ended queue, 덱)
# 스택(Stack)과 큐(Queue)를 모두 효과적으로 구현할 수 있는 자료구조
# 양쪽 끝에서 O(1) 시간 복잡도로 삽입과 삭제가 가능
#
# Stack처럼 사용: (push) append(), (pop) pop()
# Queue처럼 사용: (enqueue) append(), (dequeue) popleft()
# 양방향 큐(Deque)로 활용: appendleft(), pop(), popleft()

n, m = map(int, sys.stdin.readline().strip().split())
paper = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

cnt = 0 # 그림 갯수
max_area = 0 # 넓이 배열

def bfs(x, y):

    # 4방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([x, y])

    paper[x][y] = 0 # 방문처리
    area = 1 # 넓이 카운트 시작

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # paper 안에 위치하고 아직 방문 전일 경우 방문
            if 0<= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
                paper[nx][ny] = 0
                area += 1
                queue.append([nx, ny])

    return area


for x in range(n):
    for y in range(m):
        if paper[x][y] == 1:
            max_area = max(max_area, bfs(x, y))
            cnt += 1

print(cnt)
print(max_area)
import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

scores = []
for _ in range(n):
    scores.append(list(map(int, input().strip().split())))

scores.sort(key=lambda x: (-x[1], -x[2], -x[3]))

current_score = 0
for i in range(len(scores)):
    if i == 0:
        current_score = 1
    elif scores[i][1:] != scores[i-1][1:]:
        current_score = i+1

    if scores[i][0] == k:
        print(current_score)
        break
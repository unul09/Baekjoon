import sys

n = int(sys.stdin.readline().strip())

conf_data = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    conf_data.append([start, end])

# 끝나는 시간 오름차순
# "회의의 시작시간과 끝나는 시간이 같을 수도 있다" 조건이 있기 때문에, 2번째 조건은 시작시간 오름차순
conf_data.sort(key = lambda x: (x[1], x[0]))

# 회의 배정
result = 0
timestamp = 0
for start, end in conf_data:
    if start >= timestamp:
        result += 1
        timestamp = end

print(result)
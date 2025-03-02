import sys

n = int(sys.stdin.readline().strip())
ropes = []
for _ in range(n):
    ropes.append(int(sys.stdin.readline().strip()))

# 최대중량 = min(로프 버팀력) X 로프갯수

ropes.sort(reverse=True)

# 1개부터 늘려가며 테스트
m_max = 0
for i in range(n):
    if m_max < (i+1)*ropes[i]:
        m_max = (i+1)*ropes[i]

print(m_max)
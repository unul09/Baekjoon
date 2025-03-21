import sys
import math

h, w, n, m = map(int, sys.stdin.readline().split())

# 수용 가능한 행 수 X 수용 가능한 열 수
res = math.ceil(h/(n+1)) * math.ceil(w/(m+1))
print(res)
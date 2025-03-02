import sys

n = int(sys.stdin.readline().strip())
times = list(map(int, sys.stdin.readline().split()))

times.sort()

total_time = 0
for i in range(n):
    total_time += times[i] * (n-i)

print(total_time)
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    line = list(map(int, input().strip().split()))
    tnum = line[0]
    kids = line[1:]
    cnt = 0

    for i in range(20):
        for j in range(i):
            if kids[i] < kids[j]: cnt += 1

    print(tnum, cnt)
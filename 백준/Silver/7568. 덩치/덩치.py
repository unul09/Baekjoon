import sys
input = sys.stdin.readline

n = int(input())

sizes = []
for _ in range(n):
    sizes.append(list(map(int, input().strip().split())))

res = []
for size in sizes:
    rank = 1
    for ssize in sizes:
        if size[0] < ssize[0] and size[1] < ssize[1]:
            rank += 1
    res.append(rank)

print(" ".join(map(str, res)))
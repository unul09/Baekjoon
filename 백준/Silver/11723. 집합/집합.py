import sys

input = sys.stdin.readline
myset = set([])

m = int(input())
for _ in range(m):
    line = input().strip().split()

    if len(line) > 1:
        cmd, x = line[0], int(line[1])

        if cmd == "add": myset.add(x)
        elif cmd == "remove": myset.discard(x)
        elif cmd == "check": print(int(x in myset))
        elif cmd == "toggle":
            if x in myset: myset.discard(x)
            else: myset.add(x)

    else:
        cmd = line[0]
        if cmd == "all":
            myset.clear()
            myset.update([i for i in range(1, 21)])
        elif cmd == "empty":
            myset.clear()
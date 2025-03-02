t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)

    result = ""
    for ss in s:
        for _ in range(r):
            result += ss

    print(result)

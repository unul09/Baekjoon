n = int(input())

for i in range(n, 0, -1):
    line = " " * (n-i)
    line += "*" * i
    print(line)
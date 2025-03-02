n = int(input())

for i in range(1, n):
    line = " " * (n-i)
    line += "*" * (2*i-1)
    print(line)

for i in range(n, 0, -1):
    line = " " * (n-i)
    line += "*" * (2*i-1)
    print(line)
n = int(input())

for i in range(1, 2*n):
    if i < n:
        line = " " * (i - 1)
        line += "*" * (2 * n - 2 * i + 1)
    else:
        line = " " * (2 * n - i - 1)
        line += "*" * (2 * i - 2 * n + 1)
    print(line)
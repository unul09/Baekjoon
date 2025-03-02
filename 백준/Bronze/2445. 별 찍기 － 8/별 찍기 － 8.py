n = int(input())

for i in range(1, 2*n):
    if i < n:
        line = "*" * i
        line += " " * (2 * n - 2 * i)
        line += "*" * i
    else:
        line = "*" * (2 * n - i)
        line += " " * (2 * i - 2 * n)
        line += "*" * (2 * n - i)
    print(line)
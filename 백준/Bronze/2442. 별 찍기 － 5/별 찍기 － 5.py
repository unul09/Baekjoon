n = int(input())

for i in range(1, n+1):
    line = " " * (n-i)
    line += "*" * (2*i-1)
    print(line)
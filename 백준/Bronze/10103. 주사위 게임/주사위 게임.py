n = int(input())
A = B = 100

for _ in range(n):
    a, b = map(int, input().split())

    if a>b:
        B -= a
    elif a<b:
        A -= b

print(A, B, sep="\n")
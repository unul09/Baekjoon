r1, s = map(int, input().split())

# (r1 + r2) / 2 = s
# r1 + r2 = 2s
# r2 = 2s - r1

r2 = 2*s - r1
print(r2)
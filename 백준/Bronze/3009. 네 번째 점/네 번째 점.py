x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for xx in x:
    if x.count(xx) == 1: print(xx, end=" ")

for yy in y:
    if y.count(yy) == 1: print(yy, end=" ")

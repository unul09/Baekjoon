T = int(input())

if T % 10 != 0:
    print(-1)
    exit()

b300, b60, b10 = 0, 0, 0

while T != 0:
    if T >= 300:
        b300 += int(T / 300)
        T = T % 300
    elif T >= 60:
        b60 += int(T / 60)
        T = T % 60
    elif T >= 10:
        b10 += int(T / 10)
        T = T % 10

print(b300, b60, b10)
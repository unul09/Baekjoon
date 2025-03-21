n = int(input())

# 1 / 2 / 3 / 4 / 5
# 1 / 2~7 / 8~19 / 20~37 / 38~61
# 1개 / 6개 / 12개 / 18개 / 24개

# 0 / 1 / 2 3 / 4 5 6 / 7 8 9 10
ndiv = (n+4) // 6

cnt = 0
for i in range(100000):
    ndiv -= i
    cnt += 1
    if ndiv <= 0: break

print(cnt)
n = int(input())
i = 0

# 1~s까지 합: n*(n+1)/2
while(True):
    i += 1
    sum_i = i * (i+1) / 2

    if sum_i > n:
        print(i-1)
        break
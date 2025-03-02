import math # 유클리스 호제법으로 직접 구현도 가능

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    print(math.lcm(a, b))

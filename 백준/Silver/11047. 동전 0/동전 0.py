n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.reverse()

result = 0
for coin in coins:
    if k >= coin:
        result += k // coin
        k %= coin

    if k == 0:
        break

print(result)
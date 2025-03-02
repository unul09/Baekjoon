n = int(input())
money_best = 0

for _ in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        money = 10000 + a*1000
    elif a==b or b==c:
        money = 1000 + b*100
    elif a==c:
        money = 1000 + a * 100
    else:
        money = 100*max(a, b, c)

    money_best = money_best if money_best>money else money

print(money_best)
price, num, money = map(int, input().split())

money_needed = price*num
if money_needed > money:
    print(money_needed - money)
else:
    print(0)

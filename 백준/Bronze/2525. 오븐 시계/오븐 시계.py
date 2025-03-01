h, m = map(int, input().split())
ovenTime = int(input())

m += ovenTime

if m >= 60:
    h_plus = m // 60
    h += h_plus
    m %= 60

if h >= 24:
    h %= 24

print(h, m)

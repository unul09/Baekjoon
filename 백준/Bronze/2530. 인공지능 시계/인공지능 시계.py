h, m, s = map(int, input().split())
ovenTime = int(input())

s += ovenTime

if s >= 60:
    m_plus = s // 60
    m += m_plus
    s %= 60

if m >= 60:
    h_plus = m // 60
    h += h_plus
    m %= 60

if h >= 24:
    h %= 24

print(h, m, s)

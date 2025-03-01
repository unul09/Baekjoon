n , m = map(int, input().split())

# n*m 조각 1개 - n-1번 쪼개기 -> 1*m 조각 n개
# 1*m 조각 n개 - 각 m-1번 쪼개기 -> 1*1 조각 n*m개

result = (n-1) + n* (m-1)

print(result)
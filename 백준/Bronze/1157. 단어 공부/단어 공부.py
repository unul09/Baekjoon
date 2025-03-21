from collections import Counter

li = list(input().upper())

counter = Counter(li)
# 등장 횟수가 많은 순서대로 상위 n개의 원소를 (원소, 횟수) 형태의 튜플로 반환
common_1and2 = counter.most_common(2)

if len(common_1and2) == 1 or (common_1and2[0][1] != common_1and2[1][1]):
    print(common_1and2[0][0])
else:
    print("?")
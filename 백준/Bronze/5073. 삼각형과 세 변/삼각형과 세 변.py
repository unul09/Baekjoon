import sys

while True:
    li = list(map(int, sys.stdin.readline().split()))
    if li[0] == 0: break

    if max(li)*2 >= sum(li):
        print("Invalid")
        continue

    li_set = set(li)

    if len(li_set) == 1:
        print("Equilateral")
    elif len(li_set) == 2:
        print("Isosceles")
    else:
        print("Scalene")
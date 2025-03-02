n = int(input())
calls = list(map(int, input().split()))

m = y = 0

for call in calls:
    m += ((call//60)+1) * 15
    y += ((call//30)+1) * 10

if m < y:
    print("M", m)
elif m > y:
    print("Y", y)
else:
    print("Y M", m)
t = int(input())

for _ in range(t):
    data = []
    n = int(input())
    for _ in range(n):
        school, alc = input().split()
        data.append([school, int(alc)])

    data.sort(key = lambda x: x[1], reverse=True)
    print(data[0][0])

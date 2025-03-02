t = int(input())

for _ in range(t):
    score = 0

    result = input().split("X")
    result = [s for s in result if s]

    for Os in result:
        score += len(Os)*(len(Os)+1)//2

    print(score)
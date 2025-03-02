result = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())

    r = result[a-1:b]
    r.reverse()

    result = result[:a-1] + r + result[b:]

print(" ".join(map(str, result)))
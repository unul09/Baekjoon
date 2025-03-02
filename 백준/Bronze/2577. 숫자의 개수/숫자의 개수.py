result = 1
for _ in range(3):
    result *= int(input())

result = list(str(result))
result = list(map(int, result))

for i in range(10):
    print(result.count(i))
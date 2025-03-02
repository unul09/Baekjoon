heights = []
for _ in range(9):
    height = int(input())
    heights.append(height)

# 가짜들의 키 합
fakes_sum = sum(heights) - 100
fakes_found = False

for i in range(9):
    for j in range(i+1, 9):
        h1 = heights[i]
        h2 = heights[j]
        if h1+h2 == fakes_sum:
            heights.remove(h1)
            heights.remove(h2)
            fakes_found = True
            break
    if fakes_found:
        break

heights.sort()
for i in range(7):
    print(heights[i])
nums = []
for _ in range(9):
    num = int(input())
    nums.append(num)

nums_sorted = sorted(nums, reverse=True)
max = nums_sorted[0]

print(max)
print(nums.index(max)+1)
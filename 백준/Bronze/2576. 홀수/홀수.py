nums = []
for _ in range(7):
    num = int(input())
    if num%2 == 1:
        nums.append(num)

if len(nums) == 0:
    print(-1)
    exit()

nums_sorted = sorted(nums)

print(sum(nums))
print(nums_sorted[0])
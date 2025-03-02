nums = []
for _ in range(5):
    num = int(input())
    nums.append(num)

nums.sort()

print(sum(nums) // len(nums))
print(nums[2])
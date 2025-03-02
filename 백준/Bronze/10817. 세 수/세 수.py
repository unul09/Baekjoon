# map: iterable 입력받아, 특정 함수를 적용한 결과를 반환
nums = list(map(int, input().split()))

nums.sort()

print(nums[1])
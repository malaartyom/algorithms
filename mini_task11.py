nums = [2, 0, 2, 1, 1, 0]
if len
for i in range(len(nums)):
    if i < len(nums) // 3:
        nums[i] = 0
    elif i >= (len(nums) // 3) and i < (2 * len(nums) // 3):
        nums[i] = 1
    else:
        nums[i] = 2
print(nums)
def canJump(nums: list) -> bool:
    if len(nums) <= 1:
        return True
    pos = 0
    steps = nums[pos]
    while steps > 0:
        pos += 1
        steps -= 1
        if pos >= len(nums) - 1:
            return True
        if nums[pos] >= steps:
            steps = nums[pos]
    return False

nums = [3,2,1,0,4]
print(canJump(nums))
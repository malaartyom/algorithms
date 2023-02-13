class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            pivot = (l + r) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                r = pivot - 1
            elif nums[pivot] < target:
                l = pivot + 1
        return -1

# Ссылка на Leetcode: https://leetcode.com/problems/binary-search/submissions/897257324/
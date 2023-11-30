from typing import List


def search(a, x, lo=0):

    if lo < 0:
        raise ValueError('lo must be non-negative')
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo



class SegmentTree:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.amount = len(nums)
        self.t = [[] for _ in range(4 * self.amount)]
        self.build(1, 0, self.amount - 1)

    def build(self, v: int, tl: int, tr: int):
        if tl == tr:
            self.t[v].append(self.nums[tl])
            return
        tm = (tl + tr) >> 1
        self.build(v * 2, tl, tm)
        self.build(v * 2 + 1, tm + 1, tr)
        self.t[v] = self.merge(self.t[v * 2], self.t[v * 2 + 1])

    def merge(self, left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    def count_smaller(self, value: int, v: int, tl: int, tr: int, l: int, r: int) -> int:

        if l == tl and r == tr:
            return search(self.t[v], value)
        tm = (tl + tr) >> 1
        res = 0

        if l <= tm:
            res += self.count_smaller(value, v * 2, tl, tm, l, min(r, tm))
        if r >= tm + 1:
            res += self.count_smaller(value, v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)

        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        tree = SegmentTree(nums)
        result = []
        for index in range(len(nums)):
            result.append(tree.count_smaller(nums[index], 1, 0, tree.amount - 1, index, tree.amount - 1))
        return result
    
sol = Solution()
nums = [5,2,6,1]

print(sol.countSmaller(nums))
from typing import *



class SegmentTree:
    def __init__(self, arr):
        self.arr = [0 for i in range((len(arr)) * 4)]
        self.org = arr[:]

    def create(self, l, r, idx):
        mid = (l + r) // 2
        if l == r:
            self.arr[idx] = self.org[l]
            return
        self.create(l, mid, 2 * idx + 1)
        self.create(mid + 1, r, 2 * idx + 2)
        self.arr[idx] = self.arr[2 * idx + 1] + self.arr[2 * idx + 2]

    def query(self, ind, low, high, l, r):
        mid = (low + high) >> 1
        if low >= l and high <= r: return self.arr[ind]
        if high < l or low > r: return 0
        return self.query(2 * ind + 1, low, mid, l, r) + self.query(2 * ind + 2, mid + 1, high, l, r)

    def update(self, ind, l, r, pos, diff):
        if l == r and l == pos:
            self.arr[ind] += diff
            return
        if l <= pos <= r:
            mid = (l + r) >> 1
            self.arr[ind] += diff
            self.update(ind * 2 + 1, l, mid, pos, diff)
            self.update(ind * 2 + 2, mid + 1, r, pos, diff)


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)
        self.tree.create(0, len(nums) - 1, 0)
        self.n = len(nums)

    def update(self, index: int, val: int) -> None:
        diff = val - self.tree.org[index]
        self.tree.update(0, 0, self.n - 1, index, diff)
        self.tree.org[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(0, 0, self.n - 1, left, right)

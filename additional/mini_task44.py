from typing import List

def f(x):
    return x & (x + 1)

def g(x):
    return x | (x + 1)


class Fenwick_Tree:
    def __init__(self, n) -> None:
        self.arr = [int(0) for _ in range(n + 1)]
        self.len = len(self.arr)


    def get_prefix_sum(self, pos):
        ans = 0
        while pos > 0:
            ans += self.arr[pos]
            pos = f(pos) - 1
        return ans

    def sum(self, l, r):
        return self.get_prefix_sum(r) - self.get_prefix_sum(l)

    def increment(self, pos, val):
        pos += 1
        while pos < self.len:
            self.arr[pos] += val
            pos = g(pos)
        

    def update(self, pos, val):
        self.increment(pos, val - self.arr[pos])


class Solution:
    @staticmethod
    def createSortedArray(instructions: List[int]) -> int:
        N = max(instructions)
        tree = Fenwick_Tree(N)
        result = 0
        for i in instructions:
            result += min(tree.sum(0, i - 1), tree.sum(i, N))
            tree.increment(i - 1, 1)

        return result % (10 ** 9 + 7)


print(Solution.createSortedArray([1,2,1,2,1,2,1,2,1,2,1,2]))

# https://leetcode.com/problems/create-sorted-array-through-instructions/submissions/
from typing import *

class SegmentTree:
    
    def __init__(self, start, end, cnt):
        self.start = start
        self.end = end
        self.cnt = cnt
        self.left = None
        self.right = None
        
    def build(self, start, end):
        if start > end:
            return None
        
        root = SegmentTree(start, end, 0)
        if start == end:
            return root
        
        mid = start + (end - start) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        root.cnt = 0
        
        return root
    
    def update(self, root, num):
        if root.start > num or root.end < num:
            return
        
        if root.start == root.end:
            root.cnt += 1
            return
        
        mid = root.start + (root.end - root.start) // 2     # [start, mid], [mid+1, end]
        if num <= mid:
            self.update(root.left, num)
        elif num >= mid + 1:
            self.update(root.right, num)
            
        root.cnt = root.left.cnt + root.right.cnt
        
    def query(self, root, start, end):
        if start > root.end or end < root.start:
            return 0
        
        if start <= root.start and end >= root.end:
            return root.cnt
        
        return self.query(root.left, start, end) + self.query(root.right, start, end)

    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        if len(nums) == 1:
            return [0]
        
        min_num, max_num = min(nums), max(nums)
        
        segment_tree = SegmentTree(min_num, max_num, 0)
        root = segment_tree.build(min_num, max_num)
        
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            segment_tree.update(root, nums[i])
            cnt_of_smaller = 0
            if nums[i] > min_num:
                cnt_of_smaller = segment_tree.query(root, min_num, nums[i] - 1)
            res[i] = cnt_of_smaller
            
        return res
		
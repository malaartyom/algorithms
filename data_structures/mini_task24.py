from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        root.right = self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)
        if root.val < low or root.val > high:
            if root.val < low:
                return root.right
            else:
                return root.left
        else:
            return root
        
# https://leetcode.com/problems/trim-a-binary-search-tree/submissions/939343585/
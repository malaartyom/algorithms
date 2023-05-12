import math
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_valid(root, low, high):
    if not root:
        return True
    if (not root.left or (root.left.val < root.val)) and (not root.right or (root.right.val >= root.val)) and root.val > low  and root.val < high:
        return is_valid(root.right, root.val, high) and is_valid(root.left, low, root.val)
    else:
        return False

    
a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(6)
d = TreeNode(3)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

#https://leetcode.com/problems/validate-binary-search-tree/submissions/948371852/
print(is_valid(a, -math.inf, math.inf))
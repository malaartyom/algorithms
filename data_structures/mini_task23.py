import math
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def height(node):
    if not node:
        return 0
    left_h = height(node.left)
    right_h = height(node.right)
    return max(left_h, right_h) + 1

def max_in_BST(root):
    if not root:
        return -1
    return max(root.val, max_in_BST(root.right), max_in_BST(root.left))

def min_in_BST(root):
    if not root:
        return math.inf
    return min(root.val, min_in_BST(root.right), min_in_BST(root.left))


def is_valid(root):
    h = height(root)
    if not root:
        return True
    if max_in_BST(root.left) <= root.val and min_in_BST(root.right) >= root.val:
        return is_valid(root.right) and is_valid(root.left)
    else:
        return False

    
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
c.right = e

#https://leetcode.com/problems/validate-binary-search-tree/submissions/936860945/
print(is_valid(a))
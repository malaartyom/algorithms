import math
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def pop_left(a: list) -> list:
    del a[0]
def side_view(root):
    result = []
    if not root:
        return result
    Q = [root.val]
    while Q:

    

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
c.right = e
print(side_view(a))
#https://leetcode.com/problems/binary-tree-right-side-view/submissions/936748642/
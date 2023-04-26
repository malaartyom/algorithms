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

def print_level(root, level):
    if not root:
        return
    if level == 0:
        return str(root.val) + " " 
    elif level > 0:
        a = print_level(root.left, level - 1)
        b = print_level(root.right, level - 1)
        output = f"{a} {b} "
    return output

def levels(root):
    out = []
    h = height(root)
    for i in range(h):
        out.append(print_level(root, i).split())
    return out

def side_veiw(root):
    a = []
    lvls = levels(root)
    for i in lvls:
        index = -1
        while i[index] == "None" and abs(index) <= len(i) :
            index -= 1
        a.append(int(i[index]))
    return a

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
c.right = e
print(levels(a))
print(side_veiw(a))
#https://leetcode.com/problems/binary-tree-right-side-view/submissions/936748642/
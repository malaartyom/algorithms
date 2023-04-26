# Definition for a binary tree node.
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

def my_serialize(root):
    out = ""
    h = height(root)
    for i in range(h):
        out += print_level(root, i)
    return " ".join(out.split())

def split_by_levels(string):
    string = string.split()
    ret = []
    if len(string) != 0:
        length = int(math.log(len(string), 2)) + 1
    else:
        length = 0
    summ = 0
    for i in range(length):
        a = []
        summ += i
        for j in range(summ, summ + 2 ** i):
            a.append(string[j])
        ret.append(a)
    return ret

def my_deserialize(data):
    levels = split_by_levels(data)
    for level in levels:
        for i in range(len(level)):
            level[i] = TreeNode(int(level[i])) if level[i] != "None" else None
    if len(levels) != 0:
        root = levels[0][0]
    else:
        root = None
    for i in range(len(levels) - 1):
        k = 0
        for j in range(len(levels[i])):
            levels[i][j].left = levels[i + 1][k]
            levels[i][j].right = levels[i + 1][k + 1]
            k += 2
    return root

    
# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# d = TreeNode(4)
# e = TreeNode(5)
# a.left = b
# a.right = c
# c.left = d
# c.right = e
# data = my_serialize(a)
# print(data)
# print(split_by_levels(data))
# new_root = my_deserialize(data)
# print(my_serialize(new_root))

class Codec:

    def serialize(self, root):
        my_serialize(root)
        

    def deserialize(self, data):
        my_deserialize(data)
        
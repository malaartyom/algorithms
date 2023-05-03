# Definition for a binary tree node.

# class TreeNode():
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def my_serialize(root):
        if not root:
            return ""
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
        return " ".join(result)

def my_deserialize(data):
    if not data:
        return None
    values = data.split(" ")
    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1
    while queue:
        node = queue.pop(0)
        if values[i] != "None":
            left = TreeNode(int(values[i]))
            node.left = left
            queue.append(left)
        i += 1
        if values[i] != "None":
            right = TreeNode(int(values[i]))
            node.right = right
            queue.append(right)
        i += 1
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
# new_root = my_deserialize(data)
# print(my_serialize(new_root))

class Codec:

    def serialize(self, root):
        my_serialize(root)
        

    def deserialize(self, data):
        my_deserialize(data)
        
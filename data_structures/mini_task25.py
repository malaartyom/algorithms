class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
c.right = e


def get_len(root, array):
    if not root:
        return
    get_len(root.left, array)
    array.append(root.val)
    get_len(root.right, array)

def balance(array, start, end):
    if start > end:
        return
    middle = (end - start) // 2
    root = TreeNode(array[middle])
    root.left = balance(array[:middle], 0, middle - 1)
    root.right = balance(array[middle + 1:], middle + 1, len(array) - 1)
    return root

def upper_balance(root):
    array = []
    get_len(root, array)
    _l = len(array)
    return balance(array, 0, _l)

print(upper_balance(a))


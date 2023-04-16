class LinkedList:
    class Node:
        def __init__(self, val, nxt=None):
            self.val = val
            self.next = nxt

    def __init__(self):
        self.head = self.tail = None

    def add_to_tail(self, val, nxt=None):
        node = LinkedList.Node(val, nxt)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node

    def add_to_head(self, val):
        node = LinkedList.Node(val, self.head)
        self.head = node
        if not self.tail:
            self.tail = self.head
    
    def __str__(self):
        cur = self.head
        a = ""
        while cur.next:
            a += f'{cur.val} -> '
            cur = cur.next
        a += f"{cur.val} ->"
        return a
            

a = LinkedList()
# for i in range(1, 6):
#     a.add_to_tail(i)
a.add_to_tail(5)

print(a)

def reverse(head, counter):
    count = 0
    prv = None
    cur = head
    while count < counter:
        nxt = cur.next
        cur.next = prv
        prv = cur
        cur = nxt
        count += 1

def my_reverseBetween(head, left, right):
    if left == right:
        return head
    prv_left, _left, _right, nxt_right = None, None, None, None 
    cur = head
    for i in range(1, right + 1):
        if i == left - 1:
            prv_left = cur
        elif i == left:
            _left = cur
        elif i == right:
            _right = cur
        cur = cur.next
    if _right:
        nxt_right = _right.next
    else:
        nxt_right = _right
    reverse(_left, right - left + 1)
    _left.next = nxt_right
    if prv_left:
        prv_left.next = _right
        return head
    else:
        return _right

    
b = my_reverseBetween(a.head, 1, 1)
print(b)
#https://leetcode.com/problems/reverse-linked-list-ii/submissions/927983223/
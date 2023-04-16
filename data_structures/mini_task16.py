# class LinkedList:
#     class Node:
#         def __init__(self, val, nxt=None):
#             self.val = val
#             self.next = nxt

#     def __init__(self):
#         self.head = self.tail = None

#     def add_to_tail(self, val, nxt):
#         node = LinkedList.Node(val, nxt)
#         if self.tail:
#             self.tail.next = node
#             self.tail = node
#         else:
#             self.head = self.tail = node

#     def add_to_head(self, val):
#         node = LinkedList.Node(val, self.head)
#         self.head = node
#         if not self.tail:
#             self.tail = self.head

def detectCycle(head):
    try:
        nxt = head.next
        nxt1 = (head.next).next
        while nxt != nxt1: # found cycle
            nxt = nxt.next
            nxt1 = nxt1.next.next
        nxt = head
        count = 0
        while nxt != nxt1: # count len of cycle
            nxt = nxt.next
            nxt1 = nxt1.next
            count += 1
        cur = head
        for i in range(count):
            cur = cur.next
        return cur
    except AttributeError:
        return None
    
#https://leetcode.com/problems/linked-list-cycle-ii/submissions/927919088/
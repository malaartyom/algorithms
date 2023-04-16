
class binary_heap():

    def __init__(self) -> None:
        self.value = []
        self.priority = []
    

    def fix_up_down(self, i):
        while 2 * i + 1 < len(self.value):
            left_index = 2 * i + 1
            if 2 * i + 2 < len(self.value):
                right_index = 2 * i + 2
            else:
                right_index = i

            if self.priority[i] >= self.priority[right_index] or self.priority[i] >= self.priority[left_index]:
                if self.priority[left_index] < self.priority[right_index]:
                    self.priority[i], self.priority[left_index] = self.priority[left_index], self.priority[i]
                    self.value[i], self.value[left_index] = self.value[left_index], self.value[i]
                    i = left_index
                else:
                    self.priority[i], self.priority[right_index] = self.priority[right_index], self.priority[i]
                    self.value[i], self.value[right_index] = self.value[right_index], self.value[i]
                    if i == right_index:
                        break
                    i = right_index
            else:
                break
    def fix_down_up(self, i):
        while i != 0:
            dad_index = (i - 1) // 2
            if self.priority[dad_index] > self.priority[i]:
                self.priority[i], self.priority[dad_index] = self.priority[dad_index], self.priority[i]
                self.value[i], self.value[dad_index] = self.value[dad_index], self.value[i]
                i = dad_index
            else:
                break
    
    def insert(self, value, priority):
        if self.value:
            self.value.append(value)
            self.priority.append(priority)
            self.fix_down_up(len(self.value) - 1)
        else:
            self.value.append(value)
            self.priority.append(priority)

    def peek_min(self):
        return self.value[0]
    
    def extract_min(self):
        res = self.value[0]
        self.priority[0], self.priority[-1] = self.priority[-1], self.priority[0]
        self.value[0], self.value[-1] = self.value[-1], self.value[0]
        self.value.pop()
        self.priority.pop()
        self.fix_up_down(0)
        return res
    
    def __str__(self):
        return str(self.priority)
    
    def __bool__(self):
        return bool(len(self.priority))

#https://leetcode.com/problems/merge-k-sorted-lists/submissions/934712911/
# a = binary_heap()

# for i in range(1, 7):
#     a.insert(i, i)

# print(a)
# print(a.peek_min())
# print(a.extract_min())
# print(a)

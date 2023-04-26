import math
class stack:

    def __init__(self):
        self.storage = []
        self.minimum = []
    
    def push(self, value):
        self.storage.append(value)
        if len(self.minimum) == 0:
            self.minimum.append(value)
        else:
            if self.minimum[-1] >= value:
                self.minimum.append(value)
    
    def pop(self):
        value = self.storage.pop()
        if value == self.minimum[-1]:
            self.minimum.pop()
        return value
    
    def peek(self):
        value = self.storage[-1]
        return value
    
    def empty(self):
        return not(bool(len(self.storage)))
    
    def get_min(self):
        return self.minimum[-1]
    
    def __str__(self) -> str:
        maxx = max(self.storage)
        N = len(str(maxx)) + 2
        return_str = ""
        for i in range(len(self.storage)):
            s = f"|{self.storage[-(i + 1)]}" + " " * (N - len(str(self.storage[-(i + 1)]))) + "|"
            return_str += s
            return_str += "\n"
            return_str += "|" + N * "_" + "|"
            return_str += "\n"
        return return_str

# a = stack()
# a.push(1)
# a.push(2)
# a.push(3)
# a.push(0)
# print(a.get_min())
# print(a)
# a.pop()
# print(a.get_min())
# print(a)

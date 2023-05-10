



class FreqStack:

    def __init__(self):
        self.storage = dict()
        self.frequency = dict()
        self.max_fr = 1
        

    def push(self, val: int) -> None:
        if val not in self.frequency.keys():
            self.frequency[val] = 1
            if 1 not in self.storage.keys():
                self.storage[1] = []
            self.storage[1].append(val)
        else:
            self.frequency[val] += 1
            self.max_fr = max(self.max_fr, self.frequency[val])
            if self.frequency[val] not in self.storage.keys():
                self.storage[self.frequency[val]] = []
            self.storage[self.frequency[val]].append(val)

    def pop(self) -> int:
        if not self.storage[self.max_fr]:
            self.max_fr -= 1
        value = self.storage[self.max_fr].pop()
        self.frequency[value] -= 1
        return value
    
    def __str__(self) -> str:
        return(str(self.storage) + "\n" + str(self.frequency))
    
f = FreqStack()
f.push(56)
f.push(17)
f.push(55)
f.push(35)
f.push(96)
f.push(9)
print(f)
f.pop()
print(f)
f.push(98)
print(f)
f.pop()
f.push(40)
print(f)
f.pop()
f.push(50)
print(f)
f.pop()
f.push(14)
print(f)
f.pop()
print(f)
f.pop()
print(f)
f.pop()
print(f)
f.pop()
print(f)
f.pop()
print(f)
f.pop()
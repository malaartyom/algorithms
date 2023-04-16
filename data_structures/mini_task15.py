def reallocate(data, length):
    return_data = [0] * length
    min_len = min(length, len(data))
    for i in range(min_len):
        return_data[i] = data[i]
    return return_data
    
class DynArray:
    def __init__(self) -> None:
        self.data = [0] * 1
        self.len = 0
        self.cap = 1
    

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Wrong type of key")
        if key >= self.len:
            raise KeyError("Index is out of range!")
        return self.data[key] 
       
    def add(self, value):
        if self.len == self.cap:
            self.cap *= 2
            self.data = reallocate(self.data, self.cap)

        self.data[self.len] = value
        self.len += 1

    def remove(self):
        if self.len <=  (self.cap // 4):
            self.data = reallocate(self.data, self.cap // 2)
            self.cap //= 2
        self.len -= 1
        
a = DynArray()
for i in range(8):
    DynArray.add(a, i)
    print(a.data, a.len, a.cap)
print()
for i in range(8):
    DynArray.remove(a)
    print(a.data, a.len, a.cap)


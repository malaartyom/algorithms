from bitarray import bitarray
import math
import random 

def find_prime_in_range(lower_value, upper_value, counter):
    ret = []
    for number in range(lower_value, upper_value + 1): 
        if number > 1: 
            for i in range(2, number): 
                if(number % i) == 0: 
                    break 
            else:
                if len(ret) == counter:
                    break
                ret.append(number)
    return ret

def hash_k(add, base):
    def inter(x):
        return (x + add) % base
    
    return inter


def hash_funcs(N, k):
    arr = []
    bases = []
    funcs = []
    for i in range(k):
        arr.append(random.randrange(1, 72734))
    primes = find_prime_in_range(N, N * 2, 3)
    for i in range(3):
        bases.append(primes[i])
    for i in range(k):
        rand = random.randint(0, 2)
        funcs.append(hash_k(arr[i], bases[rand]))

    return funcs
        
        




class Bloom_Filter:

    def __init__(self,  quantity, probability) -> None:
        if probability >= 1 and probability <= 0:
            raise AttributeError("Wrong probability")
        else:
            self.N = math.ceil(-quantity * math.log2(math.e) * math.log2(probability))
            self.array = bitarray(self.N)
            self.hash_functions = list()
            self.k = math.ceil((math.log(2) * self.N) / quantity)
            self.hash_functions.extend(hash_funcs(self.N, self.k))
            print(self.hash_functions)
            print("Everything is OK :)")
    
    def insert(self, IP):
        x = int("".join(IP.split(".")))
        for i in range(self.k):
            self.array[self.hash_functions[i](x)] = 1
        return "IP inserted"

    def lookup(self, IP):
        x = int("".join(IP.split(".")))
        for i in range(self.k):
            if self.array[self.hash_functions[i](x)] == 1:
                return True
            else:
                return False


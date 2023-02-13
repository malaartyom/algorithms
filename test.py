import random
import time 
start = time.time()
def is_sorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True

def bogosort(array):
    while not is_sorted(array):
        random.shuffle(array)
    return array

a = [9, 8 , 7, 6, 727, 93, 1, 1313, 0, 7]
print(bogosort(a))
end = time.time()
print(end - start)
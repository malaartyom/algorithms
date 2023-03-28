import random
def partition(array:list, start:int, end:int):
    pivot = array[random.randint(start, end)]
    i = start
    j = end
    while True:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

def kth(array: list, k: int):
    if len(array) == 0:
        return array[0]
    p = partition(array, 0, len(array) - 1)
    
    if p+1 == k:
        return array[p]
    elif p + 1 > k:
        return kth(array[:p], k)
    else:
        return kth(array[p + 1:], k - p - 1)

def stupid_kth(array, k):
    return sorted(array)[k]

nums = [2, 432, 3, 4, 21, 42, 0, 3]
print(kth(nums, 5))
print(stupid_kth(nums, 5))


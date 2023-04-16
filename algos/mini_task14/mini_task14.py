import random
def partition(array:list, start:int, end:int):
    pivot = array[int((start + end) / 2)]
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

def kth(array: list, k: int, start, end):
    if start == end:
        return array[start]
    p = partition(array, start, end)
    
    if p+1 == k:
        return array[p]
    elif p + 1 > k:
        return kth(array, k, start, p)
    else:
        return kth(array, k - p - 1, p + 1, end)

def stupid_kth(array, k):
    return sorted(array)[k - 1]

nums = list(set([2, 432, 3, 4, 21, 42, 0, 3]))
print(sorted(nums))
print(kth(nums, 1, 0, len(nums) - 1))
print(stupid_kth(nums, 1))


import random
nums = [5, 12, 9, 13]
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
        
def quicksort(array:list, start:int, end:int):
    if start < end:
        p = partition(array, start, end)
        quicksort(array, start, p)
        quicksort(array, p + 1, end)

quicksort(nums, 0, len(nums) - 1)
print(nums)
#https://leetcode.com/problems/sort-an-array/submissions/915707212/
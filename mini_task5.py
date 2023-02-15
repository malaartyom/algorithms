def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def insertion_sort_k(arr, k):
    for i in range(k, len(arr)):
        j = i
        while j - k >= 0 and  arr[j - k] > arr[j]:
            swap(arr, j - k, j)
            j -= k

def shell_sort(nums):
    arr_of_k = []
    k = 1
    while 2 ** k - 1 < len(nums):
        arr_of_k.append(2 ** k - 1)
        k += 1
    arr_of_k.reverse()
    for i in arr_of_k:
        insertion_sort_k(nums, i)

def counter(array, sign, elem):
    if sign == "<":
        for i in array:
            if i > elem:
                return False
        return True
    elif sign == ">":
        for i in array:
            if i < elem:
                return False
        return True
    
def hIndex(citations) -> int:
    shell_sort(citations)
    citations.reverse()
    a = []
    for i in range(len(citations)):
        if counter(citations[:i + 1], ">", i + 1) and counter(citations[i + 1:], "<", i + 1):
            a.append(i + 1)
    return max(a) if len(a) != 0 else 0
print(hIndex([1, 3, 1]))

# https://leetcode.com/problems/h-index/submissions/898618834/
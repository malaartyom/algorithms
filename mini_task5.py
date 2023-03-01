def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def insertion_sort_k(arr, k):
    for i in range(k, len(arr)):
        j = i
        while j - k >= 0 and  arr[j - k] > arr[j]:
            swap(arr, j - k, j)
            j -= k

def shell_sort(nums):
    arr_of_k = [1, 4, 10, 23, 57, 132, 301, 701]
    arr_of_k.reverse()
    for i in arr_of_k:
        if i < len(nums):
            insertion_sort_k(nums, i)

def hIndex(citations) -> int:
    shell_sort(citations)
    citations.reverse()
    a = []
    for i in range(len(citations)):
        if i + 1 <= citations[i]:
            a.append(i + 1)
    return a[-1] if len(a) != 0 else 0
print(hIndex([0]))

# https://leetcode.com/problems/h-index/submissions/902839567/
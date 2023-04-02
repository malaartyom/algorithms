def wiggle_sorted(array):
    for i in range(1, len(array) - 1):
        if i % 2 == 1:
            if not(array[i - 1] < array[i] > array[i + 1]):
                return False
        if i % 2 == 0:
            if not(array[i - 1] > array[i] < array[i + 1]):
                return False
    return True

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def insertion_sort_k(arr, k):
    for i in range(k, len(arr)):
        j = i
        while j - k >= 0 and  arr[j - k] > arr[j]:
            swap(arr, j - k, j)
            j -= k

def wiggle_sort(nums):
    N = len(nums)
    nums.sort()
    first_part = nums[:N//2 if N % 2 == 0 else N // 2 + 1][::-1]
    second_part = nums[N//2 if N % 2 == 0 else N // 2 + 1:][::-1]
    i1 = 0
    i2 = 0
    for i in range(N):
        if i % 2 == 0:
            nums[i] = first_part[i1]
            i1 += 1
        else:
            nums[i] = second_part[i2]
            i2 += 1

a = [1,4,3,4,1,2,1,3,1,3,2,3,3]
wiggle_sort(a)
print(a)
#https://leetcode.com/problems/wiggle-sort-ii/submissions/898619405/
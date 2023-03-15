nums = [1,2,2,2,2,0,0,0,1,1]
nums1 = [2, 1, 2]
nums2 = []
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def sorting(array):
    j = len(array) - 1
    i = 0
    k = 0
    count = 0
    while i < j and k < len(array) and k <= j:
        if array[k] == 2:
            if array[j] != 2:
                swap(array,k, j)
                j -= 1
            else:
                j -= 1
                continue
            if count != 0:
                count -= 1
                continue
        if array[k] == 0:
            swap(array, k, i)
            i += 1
            if count != 0:
                count -= 1
                continue
        if array[k] == 1:
            count += 1
        k += 1
sorting(nums)
sorting(nums1)
print(nums1)
print(nums)
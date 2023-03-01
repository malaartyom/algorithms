def merge_and_count_split(left, right, res):
    count = 0
    lsize, rsize = len(left), len(right)
    n = len(res)
    i, j, k = 0, 0, 0
    while k < n and i < lsize and j < rsize:
        if left[i] < right[j]:
            res[k] = left[i]
            k += 1
            i += 1
        else:
            res[k] = right[j]
            k += 1
            j += 1
            count += len(left) - i
    while i < lsize:
        res[k] = left[i]
        i += 1
        k += 1
    while j < rsize:
        res[k] = right[j]
        j += 1
        k += 1
        count += 1
    return count




def sort_and_count_inversions(array):
    if len(array) == 1:
        return 0

    middle = int(len(array) / 2)
    left = sort_and_count_inversions(array[:middle])
    right = sort_and_count_inversions(array[middle:])

    buffer = [0 for i in range(len(array))]
    split = merge_and_count_split(array[:middle], array[middle:], buffer)
    for i in range(len(array)):
        array[i] = buffer[i]
    return left + right + split

def count_inv(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] > array[j] and i < j:
                count += 1
    return count

def count_local_inversions(array):
    count = 0
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            count += 1

    return count 

a = [1, 2, 0]
print(count_inv(a))
print(count_local_inversions(a))
print(sort_and_count_inversions(a))
print(a)
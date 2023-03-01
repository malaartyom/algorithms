def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def merge(array, start1, end1, start2, end2, start3, end3):
    n = end3 - start3
    lsize = end1 - start1 + 1
    rsize = end2 - start2 + 1
    i, j, k = 0, 0, 0
    while k < n and i < lsize and j < rsize:
        if array[start1 + i] < array[start2 + j]:
            array[start3 + k], array[start1 + i] = array[start1 + i], array[start3 + k]
            k += 1
            i += 1
        else:
            array[start3 + k], array[start2 + j] = array[start2 + j], array[start3 + k]
            k += 1
            j += 1
    while i < lsize:
        array[start3 + k], array[start1 + i] = array[start1 + i], array[start3 + k]
        k += 1
        i += 1
    while j < rsize:
        array[start3 + k], array[start2 + j] = array[start2 + j], array[start3 + k]
        k += 1
        j += 1

    
def under(array, quater, middle):
    if middle == 1:
        tmp = array[0]
        for i in range(len(array) - 1):
            array[i] = a[i + 1]
        array[-1] = tmp
        return
    array[:quater], array[quater:middle] = merge_sort(array[quater:middle]), array[:quater]
    merge(array, 0, quater - 1, middle, len(array) - 1, quater, len(array) - 1)
    under(array, int(quater/2), int(middle / 2))


def merge_sort(array):
    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[0] > array[1]:
            swap(array, 0, 1)
        return array
    middle = int(len(array) / 2)
    quater = int(len(array) / 4)
    array[:quater] = merge_sort(array[:quater])
    array[quater:middle] = merge_sort(array[quater:middle])
    merge(array, 0, quater - 1, quater, middle - 1, middle, len(array) - 1)
    array[:quater], array[quater:middle] = merge_sort(array[quater:middle]), array[:quater]
    merge(array, 0, quater - 1, middle, len(array) - 1, quater, len(array) - 1)
    # array[:quater], array[quater:middle] = merge_sort(array[quater:middle]), array[:quater]
    # merge(array, 0, quater - 1, middle, len(array) - 1, quater, len(array) - 1)
    # array[:eight], array[eight:quater] = merge_sort(array[eight:quater]), array[:eight]
    # merge(array, 0, eight - 1, quater, len(array) - 1, eight, len(array) - 1)
    # print(eight)
    return array
    # array[quater:middle] = merge_sort(array[quater:middle], array[middle])
    # array = merge(array[:quater], array[quater:middle], buffer, 0)
    # array[:quater], array[quater:middle] = merge_sort(array[quater:middle], array[:quater]), array[:quater]
    # array = merge(array[:quater], array[middle:], array[quater:], 1)
    # for i in range(len(array)):
    #     array[i] = buffer[i]
    # return array

a = [7,6,5,4,3,2,1]
print(len(a))
a = merge_sort(a)
print(a)
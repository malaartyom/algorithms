from random import randint


def swap(array: list, i: int, j: int):
    array[i], array[j] = array[j], array[i]

def merge(array: list, i, m, j, n, dist):
    while i < m and j < n:
        if array[i] <= array[j]:
            swap(array, dist, i)
            i += 1
            dist += 1
        else:
            swap(array, dist, j)
            j += 1
            dist += 1
    
    while i < m:
        swap(array, i, dist)
        i += 1
        dist += 1

    while j < n:
        swap(array, j, dist)
        j += 1
        dist += 1

def sort_trivial(array, frm, to, dist):
    while frm < to:
        swap(array, frm, dist)
        frm += 1

def sort(array, frm , to):
    if to - frm <= 1:
        return
    
    m = frm + (to - frm) // 2
    dist = frm + to - m
    sort_range(array, frm, m, dist)

    while dist - frm > 1:
        n = dist
        dist = frm + (n - frm + 1) // 2

        sort_range(array, dist, n, frm)

        merge(array, frm, frm + n - dist, n, to, dist)

        n = dist
        while n > frm:
            x = n
            while x < to and array[x] < array[x - 1]:
                swap(array, x, x - 1)
                x += 1
            n -= 1

def sort_range(array, frm, to, dist):
    if to - frm <= 1:
        sort_trivial(array, frm, to, dist)
    
    m = frm + (to - frm) // 2
    sort(array, frm, m)
    sort(array, m, to)
    merge(array, frm, m, m, to, dist)


a = [3, 5, 9, 13, 1, 0, 1, 32]
sort(a, 0, len(a))
print(a)

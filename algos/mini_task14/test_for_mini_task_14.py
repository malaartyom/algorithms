import mini_task14
import random

def stupid_kth(array, k):
    return sorted(list(set(array)))[k-1]

a = [[2, 432, 3, 4, 21, 42, 0, 3],
     [0, 0 ,0, 3, 2],
     [3, 4, 5],
     [0, 0, 0, 0]]
def make(n):
    k = 3
    b = stupid_kth(a[n], k)
    c = mini_task14.kth(a[n], k)
    assert b == c

def test1():
    make(0)

def test2():
    make(1)

def test3():
    make(2)

def test4():
    make(3)
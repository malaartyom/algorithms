from mini_task14 import *

a = [[2, 432, 3, 4, 21, 42, 0, 3],
     [0, 0 ,0, 3, 2],
     [3, 4, 5],
     [0, 0, 0, 0]]
def make(n):
    k = 3
    b = stupid_kth(a[n], k)
    c = kth(a[n], k, 0, len(a[n]) - 1)
    assert b == c

def test1():
    make(0)

def test2():
    make(1)

def test3():
    make(2)

def test4():
    make(3)
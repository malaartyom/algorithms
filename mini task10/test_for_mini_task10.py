from mini_task10 import *

a = [[],
     ["abc", "fhh", "iwi", "aaa", "pwd", "pep", "pip"],
     ["b", "f", "g", "l", "a"],
     ["", "", ""],
     ["osqko", "qisiw", "iqaih", "jdwid", "dwdwd", "asaea"],
     ["xa"]]

def make(n):
    b = sorted(a[n])
    c = LSD(a[n])
    assert b == c

def test1():
    make(0)

def test2():
    make(1)

def test3():
    make(2)

def test4():
    make(3)

def test5():
    make(4)

def test6():
    make(5)
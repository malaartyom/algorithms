from mini_task28 import Bloom_Filter

def test1():
    a = Bloom_Filter(1000, 0.01)
    a.insert("192.168.0.1")
    assert True == a.lookup("192.168.0.1")


def test2():
    a = Bloom_Filter(1000, 0.01)
    a.insert("192.168.0.1")
    assert False == a.lookup("192.168.0.2")


def test3():
    a = Bloom_Filter(1000, 0.01)
    a.insert("192.168.0.1")
    a.insert("192.168.0.2")
    a.insert("192.168.0.3")
    assert [True, True, True] == [a.lookup("192.168.0.1"), a.lookup("192.168.0.2"), a.lookup("192.168.0.3")]

def test4():
    a = Bloom_Filter(1000, 0.01)
    a.insert("192.168.0.1")
    a.insert("192.168.0.2")
    a.insert("192.168.0.3")
    assert False == a.lookup("192.168.0.4")

    

    
    

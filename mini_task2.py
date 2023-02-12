import math
import random
def mul_by_ten(x, n):
    for i in range(n):
        x = ((x << 3) + (x << 1))
    return x

def Karatsubo(x, y):
    x = str(x)
    y = str(y)
    if len(x) > len(y):
        while len(y) != len(x):
            y = '0' + y
    elif len(y) > len(x):
        while len(x) != len(y):
            x = '0' + x
    N = len(x)
    if len(x) == 1:
        return int(x) * int(y)
    else:
        a = x[:N // 2]
        b = x[N//2:]
        c = y[:N//2]
        d = y[N//2:]
        first = Karatsubo(a, c)
        second = Karatsubo(b, d)
        third = Karatsubo(int(a) + int(b), int(c) + int(d))
        fourth = third - second - first
        fith = mul_by_ten(first, len(b) + len(d)) + second + mul_by_ten(fourth, (N // 2) if N % 2 == 0 else (N // 2) + 1)
        return fith

print(Karatsubo(123, 675))
def test(x, y):
    print(f"x = {x}, y = {y}")
    # print(f"Without Karatsubo answer = {x * y}")
    # print(f"With Karatsubo answer = {Karatsubo(x, y)}")
    print(f"Equation is {x * y == Karatsubo(x, y)}")

a = [(0, 0), (0, 15), (1, 1), (6,7), (19, 82), (15662, 8), (1234, 5678), (1,1345), (16, 0), (1281102, 0), (123, 675), (12345, 987), (7127, 182) ]
for x, y in a:
    test(x, y)
    print()
for i in range(15):
    test(random.randint(0, 10000000), random.randint(0, 100000000))
    print()

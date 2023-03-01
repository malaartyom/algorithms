import random
def mul_by_ten(x, n):
    for i in range(n):
        x = ((x << 3) + (x << 1))
    return x

def int_len(x):
    count = 0
    while x != 0:
        x = x // 10
        count += 1
    return count

def Karatsubo(x, y):
    N = max(int_len(x), int_len(y))
    if N <= 2:
        return x * y
    else:
        if N % 2 != 0:
            N += 1
        a = x // (10 ** (N // 2))
        b = x % (10 ** (N // 2))
        c = y // (10 ** (N // 2))
        d = y % (10 ** (N // 2))
        first = Karatsubo(a, c)
        second = Karatsubo(b, d)
        third = Karatsubo(a + b, c + d)
        fourth = third - second - first
        fith = mul_by_ten(first, N) + second + mul_by_ten(fourth, (N // 2) if N % 2 == 0 else (N // 2) + 1)
        return fith

print(Karatsubo(15662, 8))
def test(x, y):
    print(f"x = {x}, y = {y}")
    print(f"Without Karatsubo answer = {x * y}")
    print(f"With Karatsubo answer = {Karatsubo(x, y)}")
    assert(x * y == Karatsubo(x, y))

a = [(0, 0), (0, 15), (1, 1), (6,7), (19, 82), (15662, 8), (1234, 5678), (1,1345), (16, 0), (1281102, 0), (123, 675), (12345, 987), (7127, 182) ]
for x, y in a:
    test(x, y)
    print()
for i in range(15):
    test(random.randint(0, 10000000), random.randint(0, 100000000))
    print()

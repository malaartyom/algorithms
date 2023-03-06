def inc(x, y, z):
    return x + y + z

a = [(1, 2, 3), (4, 5, 6)]
b = []
b.append(inc)
print(b[0](*a[0]))

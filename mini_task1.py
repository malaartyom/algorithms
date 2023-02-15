def counting(a,b):
    count = 0
    while a > b:
        a -= b
        count += 1
    return count

def division(a, b):
    answ = []
    n = len(str(a))
    m = len(str(b))
    if a < b:
        return 0
    else:
        k = n - 1
        while a > b:
            while (counting(a,(10 ** k))) < b:
                k -= 1 # в худшем случае m операций вычитания из k
            res = counting(counting(a,(10 ** k)), b)
            answ.append(res)
            a -= b * res * 10 ** k # в худшем случае порядка n вычитаний => порядка n итераций верхнего цикла while
    return ''.join([str(i) for i in answ])
# => ~ m * n элементарных операций
print(division(1234, 11))
        


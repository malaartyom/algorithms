
def numTrees(n: int) -> int:
    table = [0] * (n + 1)
    table[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            table[i] += table[j] * table[i - j - 1]

    return table[n - 1]
        
numTrees(4)
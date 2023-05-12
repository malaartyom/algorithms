def find(s):
    i = 0
    ret = dict()
    a = []
    while i + 10 <= len(s):
        if s[i:i+10] not in ret.keys():
            ret[(s[i:i+10])] = 1
        else:
            ret[(s[i:i+10])] += 1
        i+=1
    for i in ret:
        if ret[i] > 1:
            a.append(i)
    return a
#https://leetcode.com/problems/repeated-dna-sequences/submissions/947277766/


print(find("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

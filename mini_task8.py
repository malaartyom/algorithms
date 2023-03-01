def merge(A, buffer, start, middle, end):
    k = i = start
    j = middle + 1
    inversionCount = 0
    while i <= middle and j <= end:
        if A[i] <= A[j]:
            buffer[k] = A[i]
            i = i + 1
        else:
            buffer[k] = A[j]
            j = j + 1
            inversionCount += (middle - i + 1) 
        k = k + 1
    while i <= middle:
        buffer[k] = A[i]
        k = k + 1
        i = i + 1
    for i in range(start, end + 1):
        A[i] = buffer[i]
 
    return inversionCount
 

def countGlobalInversions(A, buffer, start, end):
    invs = 0
    if end <= start:
        return 0
    middle = start + ((end - start) // 2)
    invs  += countGlobalInversions(A, buffer, start, middle)
    invs += countGlobalInversions(A, buffer, middle + 1, end)
    invs += merge(A, buffer, start, middle, end)
 
    return invs

def countLocalInversions(A):
    InversionsCount = 0
    if len(A) != 2:
        for i in range(1, len(A)):
            if A[i - 1] > A[i]: 
                InversionsCount += 1
    else:
        if A[0] > A[1]:
            InversionsCount += 1
    return InversionsCount

def CountInversions(A):
    B = A.copy()
    return countGlobalInversions(A, B, 0, len(A) - 1)

class Solution:
    def isIdealPermutation(self, nums) -> bool:
        # for i in range(len(nums)):
        #     if abs(i - nums[i]) > 1:
        #         return False
        # return True
        localinv = int(countLocalInversions(nums))
        globalinv = int(CountInversions(nums))
        if localinv == globalinv:
            return True
        else:
            return False
        
# print(CountInversions([1, 0, 2]))
# print(countLocalInversions([1, 0, 2]))
a = [2, 0, 1]
localinv = int(countLocalInversions(a))
globalinv = int(CountInversions(a))
print(globalinv, localinv)
if localinv == globalinv:
    print(True)
else:
    print(False)
def counting_sort(nums: list, ksi, u):
    C = [0] * (max([ksi(i, u) for i in nums])  + 1) 
    R = [0] * len(nums)
    for i in nums:
        C[ksi(i, u)] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    k = - 1
    while k >= -len(nums):
        R[C[ksi(nums[k], u)] - 1] = nums[k]
        C[ksi(nums[k], u)] -= 1
        k -= 1
    return R

def func(string, k):
    return ord(string[k])

def LSD(array):
    k = -1
    while k >= -len(array):
        counting_sort(array, func, k)
        k -= 1
    return array
        
a = ["abf", "dec"]
b = a.copy()
b.sort()
print(b)
print(LSD(a))



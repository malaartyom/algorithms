frequency = {1:3, 2:0, 3:7, 4:2}
maxx = max(frequency, key=lambda x: frequency[x])
print(maxx)
# a = 20
# def div10(a):
#     if a < 10:
#         return 0
#     if a == 10:
#         return 1
#     return 1 + div10(a - 10)

# # print(div10(a))
# # from tqdm import tqdm
# # summ = 0
# # i = 0
# # e = 0.000000000001
# # x = 1
# # while abs(x) > e:
# #     x = ((-1) ** i) / ((2 * i + 1) ** 2)
# #     summ += x
# #     i += 1

# # # print(summ)
# # nodes = [1, 2, 3]
# # nodes.pop()
# # print(nodes)
# j = 2
# for i in range(0, 16, 2):
#     print(f"        Or(a=out1[{i}], b=out1[{i+1}], out=out{j});")
#     j += 1
    
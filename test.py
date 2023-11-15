# import csv
# import matplotlib.pyplot as plt

# with open("/Users/artemmalarenko/Documents/GitHub/algorithms/20231016-0003(2).csv") as file:
#     reader = list(csv.reader(file, delimiter=";"))
#     r = reader[:4]
#     reader = reader[3:]
#     reader = [[float(j.replace(",", ".")) for j in i] for i in reader]
#     x = []
#     y = []
#     for i, j in reader:
#         x.append(i)
#         y.append(j)
#     plt.plot(x, y)
#     plt.show()
#     # print(r)
    
#     max_y = max(reader, key= lambda x: x[1])[1]
#     list_of_extremums = []
#     print(max_y)

#     for row in reader:
#         if row[1] == max_y:
#             list_of_extremums.append(row)
#     print(list_of_extremums[:5])
#     print(list_of_extremums[1][0] - list_of_extremums[0][0])


c = 10
b = 3
a = c
c += b
print(c)
c = a
c -= b
print(c)
c = a
c *= b
print(c)
# дальше аналогично 


























from mini_task18 import *

tests = [
    "2+3*4",
    "(8-4*2)/(1+3*2)",
    "10&6|3^2",
    "5*(4-2)+(6-3)*2",
    "8<<2",
    "2**3*4"
]
for i in range(len(tests)):
    print(main(tests[i]))
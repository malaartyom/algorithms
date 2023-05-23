import subprocess as sb
import time as tm
import os
from tqdm import tqdm
from datetime import datetime

S = 1
Hoare = 0
Lomuto_st = 0
Lomuto_bf = 0
os.chdir("/Users/artemmalarenko/Documents/GitHub/algorithms/algos/mini_task13")
for i in tqdm(range(S)):
    sb.run(["g++", "mini_task13_hoare.cpp"], capture_output=True)
    start = tm.time()
    sb.run(["./a.out"], capture_output=True)
    end = tm.time()
    Hoare += end - start
    # print(f"Hoare: {end - start}")
    sb.run(["g++", "mini_task13_lomuto0.cpp"], capture_output=True)
    start = tm.time()
    sb.run(["./a.out"], capture_output=True)
    end = tm.time()
    Lomuto_st += end - start
    # print(f"Standart Lomuto: {end - start}")
    sb.run(["g++", "mini_task13_lomuto.cpp", "-Ofast"], capture_output=True)
    start = tm.time()
    sb.run(["./a.out"], capture_output=True)
    end = tm.time()
    Lomuto_bf += end - start
    # print(f"Lomuto branchfree: {end - start}")

# print(f" Hoare: {Hoare / S}; \n Lomuto standart: {Lomuto_st / S}; \n Lomuto branchfree {Lomuto_bf / S};")
f = open("/Users/artemmalarenko/Documents/GitHub/algorithms/algos/mini_task13/output.txt", "a")
f.write("__________________________________________________________")
f.write(f"\nHoare: {Hoare / S}; \n")
f.write(f"Lomuto standart: {Lomuto_st / S}; \n")
f.write(f"Lomuto branchfree {Lomuto_bf / S}; \n")
f.write(f"Time is {datetime.now()}")
f.write("\n")
f.write("__________________________________________________________")
f.close()
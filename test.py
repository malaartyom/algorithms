print("p  q  r  1  2  3  4  5  6")
print("-------------------------")
for p in range(2):
    for q in range(2):
        for r in range(2):
            print(f"{p}  {q}  {r}  {int(q <= r)}  {int(p <= abs(r - 1))}  {int(p <= abs(q - 1))}  {int(p <= (q <= r))}  {int((p <= abs(r - 1)) <= (p <= abs(q - 1)))}  {int((p <= (q <= r)) <= ((p <= abs(r - 1)) <= (p <= abs(q - 1))))}")
n=int(input("ixtiyoriy butun sonni kiriting - "))
t=0

for son in range(2, n+1):
    k=son%2
    if k==0:
        t+=son
    else :
        continue
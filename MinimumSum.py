import math
n,x=map(int,input().split())
a=list(map(int,input().split()))
Sum=0
for i in range(n):
    k=float(a[i]/x)
    if a[i]>=0:
        y=int(math.floor(k))
    else:
        y=int(math.ceil(k))
    Sum=Sum+(x*y)
print(Sum)
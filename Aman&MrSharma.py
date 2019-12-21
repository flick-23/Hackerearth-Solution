d=int(input())
t=0
for D in range(d):
    r=int(input())
    x=int(input())
    d=2*(22/7)*r
    x*=100
    if(d<=x):
        t+=1
print(t)
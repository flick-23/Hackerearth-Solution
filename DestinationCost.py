n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]<b[i]:
        c+=a[i]
    else:
        c+=b[i]
print(c)
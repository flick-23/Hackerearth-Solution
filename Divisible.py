n=int(input())
a=list(map(str,input().split()))
num=0
for i in range(n):
    if i < (n/2):
        x=int(a[i][0])
    else:
        x=int(a[i][-1])
    num=(num*10)+x
if(num%11==0):
    print("OUI")
else:
    print("NON")
    
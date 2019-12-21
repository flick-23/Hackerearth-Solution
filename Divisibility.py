n=int(input())
a=list(map(int,input().split()))
num=0
for i in a:
    rem=i%10
    num=(num*10)+rem
if num %10==0:
    print("Yes")
else:
    print("No")
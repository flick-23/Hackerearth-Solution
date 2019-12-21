n=int(input())
a=list(map(int,input().split()))
product=1
for i in a:
    product*=i
print(product%(10**9 + 7))
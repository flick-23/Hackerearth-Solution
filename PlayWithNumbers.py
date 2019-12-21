#incomplete USE FAST i/o
from sys import stdin, stdout 
import  math
n,q=map(int,input().split())
a=list(map(int,input().split()))
for Q in range(q):
    l,r=map(int,stdin.readline().split())
    sum=0
    i=0
    while(l<=r):
        sum+=a[l-1]
        i+=1
        l+=1
    stdout.write(math.floor(sum/i)+'\n')
    
import math
t=int(input())
a=0
b=7
for T in range(t):
    n=int(input())
    A=abs(n-a)
    B=abs(b-n)
    if A<B:
        print("A")
        a=n
    elif B<A:
        print("B")
        b=n
    elif A==B:
        if a<n:
            print("A")
            a=n
        elif b<n :
            print("B")
            b=n
t=int(input())
for T in range(t):
    n=int(input())
    while(1):
        if(n%2==0):
            n/=2
        else:
            n=(3*n)+1
        if(n==1):
            print("YES")
            break
        if(n<1):
            print("NO")
    
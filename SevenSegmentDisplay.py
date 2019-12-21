t=int(input())
for T in range(t):
    N=int(input())
    s=0
    while(1):
        n=int(N%10)
        if n==0:
            s=s+6
        elif n==1:
            s=s+2
        elif n==2:
            s=s+5
        elif n==3:
            s=s+5
        elif n==4:
            s=s+4
        elif n==5:
            s=s+5
        elif n==6:
            s=s+6
        elif n==7:
            s=s+3
        elif n==8:
            s=s+7
        elif n==9:
            s=s+6
        N=int(N/10)
        if N==0:
            break
    if s%2==0:
        while(s!=0):
            print("1",end='')
            s-=2
    if s%2 !=0:
        print("7",end='')
        s-=3
        while(s!=0):
            print("1",end='')
            s-=2
    print()
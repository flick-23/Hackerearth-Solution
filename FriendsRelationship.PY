t=int(input())
for T in range(t):
    n=int(input())
    rs=0
    re=(2*n)-1
    for i in range(n):
        for j in range(2*n):
            if(j<=i):
                print("*",end="")
                rs+=1
            elif(j>=re):
                print("*",end="")
            else:
                print("#",end="")
        re-=1
        print()
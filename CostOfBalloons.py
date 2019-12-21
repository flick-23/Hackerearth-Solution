t=int(input())
for T in range (t):
    g,p=map(int,input().split())
    n=int(input())
    count_p1=0
    count_p2=0
    for i in range(n):
        p1,p2=map(int,input().split())
        if(p1==1):
            count_p1+=1
        if(p2==1):
            count_p2+=1
    if(count_p1>count_p2):
        if(g>p):
            sum=(count_p1*p)+(count_p2*g)
        else:
            sum=(count_p1*g)+(count_p2*p)
    else:
        if(g>p):
            sum=(count_p1*g)+(count_p2*p)
        else:
            sum=(count_p1*p)+(count_p2*g)
    print(sum)
n,q=map(int,input().split())
a=list(map(int,input().split()))
for Q in range(q):
    Sum=0
    c,x,y=map(int,input().split())
    if c==1:
        a[x]=y
    else:
        if(y<n):
            while(x<=y):
                Sum+=a[x]
                x+=1
            print(Sum)
        else:
            print("-1")
        
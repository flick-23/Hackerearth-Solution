t=int(input())
for T in range(t):
    a,b=map(int,input().split())
    if a>b:
        c=int(a/b)
    else:
        c=int(b/a)
    print(c)
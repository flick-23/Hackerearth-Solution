l=int(input())
n=int(input())
for N in range(n):
    w,h=map(int,input().split())
    if(w*h == l*l or (w==h and (w>l and h>l))):
        print("ACCEPTED")
    elif w<l or h<l:
        print("UPLOAD ANOTHER")
    else:
        print("CROP IT")
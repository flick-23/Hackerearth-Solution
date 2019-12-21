n=input()
if len(n)!=10:
    print("Illegal ISBN")
else:
    i=1
    sum=0
    while(i<=10):
        a=int(n[i-1])
        sum+=i*a
        i+=1
    if sum%11==0:
        print("Legal ISBN")
    else:
        print("Illegal ISBN")
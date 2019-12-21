t=int(input())
for T in range(t):
    s1,s2=map(str,input().split())
    l=len(s1)
    i=97
    flag=0
    while(i<=122):
        j=0
        c1=0
        while(j<l):
            n=ord(s1[j])
            if n==i:
               # print(f"N :{n}, char :{s1[j]}")
                c1+=1
            j+=1
        j=0
        c2=0
        while(j<l):
            n=ord(s2[j])
            if n==i:
                #print(f"N :{n}, char :{s2[j]}")
                c2+=1
            j+=1
        if(c2>0 or c1>0):
            if(c1!=c2):
                flag=1
                print("NO")
                break
        i+=1
    if(flag==0):
        print("YES")
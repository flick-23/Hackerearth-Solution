s=input()
i=0
flag=0
while(i<9):
    if (i<1) or (i>=3 and i<=4) or (i==7):
        a=int(s[i])
        b=int(s[i+1])
        if (a+b)%2 !=0 :
            flag=1
            print("invalid")
            break
    if(i==2):
         if(s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U' or s[i]=='Y'):
            flag=1
            print("invalid")
            break
    i+=1
if flag==0:
    print("valid")
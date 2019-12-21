n=int(input())
i=1
c=0
while(1):
    if(i%3!=0):
        print("*   *")
    else:
        c+=1
        if(c>n):
            break
        else:
            print("*****")
    i+=1
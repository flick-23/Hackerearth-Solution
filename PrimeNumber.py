n=int(input())
i=2
while(i<n):
    flag=0
    count=0
    j=2
    while(j<i):
        if i % j == 0:
            flag=1
            break;
        j+=1
    if flag==0:
        print(i,end=' ')
    i+=1

    

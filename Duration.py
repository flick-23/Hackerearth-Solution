t=int(input())
for T in range(t):
    sh,sm,eh,em=map(int,input().split())
    min=60-sm
    sh+=1
    hour=eh-sh
    min+=em
    if(min>=60):
        while(min>=60):
            min=min-60
            hour=hour+1
    print(hour,min)
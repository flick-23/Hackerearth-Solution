WS_left=[1]
WS_right=[6]
MS_left=[2]
MS_right=[5]
AS_left=[3]
AS_right=[4]

i=1
j=6
k=0
while(k<=18):      #Initialisation for Windows seating arrangement
    i+=11
    if(i<=108):
        WS_left.append(i)
    i+=1
    if(i<=108):
        WS_left.append(i)
    j+=1
    if(j<=108):
        WS_right.append(j)
    j+=11
    if(j<=108):
        WS_right.append(j)
    k+=1

i=2
j=5
k=0
while(k<=18):  #initialisation for Middle seat arrangement
    i+=9
    if(i<=108):
        MS_left.append(i)
    i+=3
    if(i<=108):
        MS_left.append(i)
    j+=3
    if(j<=108):
        MS_right.append(j)
    j+=9
    if(j<=108):
        MS_right.append(j)
    k+=1

i=3
j=4
k=0
while(k<=18):
    i+=7
    if(i<=108):
        AS_left.append(i)
    i+=5
    if(i<=108):
        AS_left.append(i)
    j+=5
    if(j<=108):
        AS_right.append(j)
    j+=7
    if(j<=108):
        AS_right.append(j)
    k+=1
t=int(input())
for T in range(t):
    n=int(input())
    for i in range(20):
        if WS_left[i]==n:
            if(i%2==0):
                print(WS_left[i+1],"WS")
                break
            else:
                print(WS_left[i-1],"WS")
                break
        elif WS_right[i]==n:
            if i%2==0:
                print(WS_right[i+1],"WS")
                break
            else:
                print(WS_right[i-1],"WS")
                break
        elif MS_right[i]==n:
            if i%2==0:
                print(MS_right[i+1],"MS")
                break
            else:
                print(MS_right[i-1],"MS")
                break
        elif MS_left[i]==n:
            if i%2==0:
                print(MS_left[i+1],"MS")
                break
            else:
                print(MS_left[i-1],"MS")
                break
        elif AS_right[i]==n:
            if i%2==0:
                print(AS_right[i+1],"AS")
                break
            else:
                print(AS_right[i-1],"AS")
                break
        elif AS_left[i]==n:
            if i%2==0:
                print(AS_left[i+1],"AS")
                break
            else:
                print(AS_left[i-1],"AS")
                break
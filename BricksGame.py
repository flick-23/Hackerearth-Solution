n=int(input())
i=1
while(1):
    n-=i
    j=i*2
    #print(f"Bricks remaining after Patlu keeps : {i} bricks are : {n}")
    if n<1 :
        print('Patlu')
        break
    n-=j
    #print(f"Bricks remaining after Patlu keeps : {j} bricks are : {n}")
    i+=1
    if n<1 :
        print('Motu')
        break
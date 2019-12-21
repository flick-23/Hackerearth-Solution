#Encrypts the alphanumeric terms from string by 'k' terms 

s=input()
k=int(input())
K=k
S=""

while(1):
    if k>=0 and k<=26:
        break
    k-=26
    
while(1):
    if K>=0 and K<=9:
        break
    K-=10
    
for i in s:
    ch=ord(i)
    if ch>=65 and ch<=90:
        ch+=k
        if ch>90:
            ch=(ch-90)+64
    if ch>=97 and ch<=122:
        ch+=k
        if ch>122:
            ch=(ch-122)+96
    if ch>=48 and ch<=57:
        ch+=K
        if ch>57:
            ch=(ch-57)+47
    c=chr(ch)
    S+=c
print(S)
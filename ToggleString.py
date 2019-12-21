s=input()
S=""
l=len(s)
c=0
for i in range(l):
    c=ord(s[i])
    if c>=65 and c<=90:
        c+=32
        c=chr(c)
        S+=c
    else:
        c-=32
        c=chr(c)
        S+=c
print(S)
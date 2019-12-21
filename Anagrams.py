#Wrong logic , correct logic in Java folder in JAVA
t=int(input())
for T in range(t):
    a=input()
    b=input()
    c=0
    l_a=len(a)
    l_b=len(b)
    if l_a>l_b:
        for i in range(l_a):
            for j in range(l_b):
                if a[i]==b[j]:
                    c+=1
                    a.replace(a[i],'0')
                    b.replace(a[j],'0')
                    break
    else:
        for i in range(l_b):
            for j in range(l_a):
                if b[i]==a[j]:
                    c+=1
                    b.replace(b[i],'0')
                    a.replace(a[j],'0')
                    break
    c*=2
    l=((l_a+l_b)-c)
    print(a)
    print(l)
    
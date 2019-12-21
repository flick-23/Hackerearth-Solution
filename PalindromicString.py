s=input()
S=""
for i in range(len(s)):
    S+=s[-1-i]
if s==S:
    print("YES")
else:
    print("NO")
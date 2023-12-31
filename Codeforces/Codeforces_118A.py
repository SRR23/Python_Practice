
x=input()
s=x.lower()
mp={'a':1,'e':1,'i':1,'o':1,'u':1,'y':1}
ans=''
for i in s:
    if i not in mp:
        ans+='.'+i

print(ans)
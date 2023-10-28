

s=input()
ans=[]
x=y=0
st=""
for i in range(len(s)):
    if s[i]=='L':
        x+=1
        st+='L'
    else:
        y+=1
        st+='R'
    if(x==y):
        ans.append(st)
        x=y=0
        st=""

print(len(ans))
for i in range(len(ans)):
    print(ans[i])
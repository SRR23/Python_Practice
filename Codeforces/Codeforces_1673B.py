

t=int(input())
while t>0:
    t-=1
    s=input()
    mp,k={},0
    while k<len(s):
        if s[k] in mp:
            break
        else:
            mp[s[k]]=1
            k+=1
    
    i=k
    f=True
    while i<len(s):
        if s[i]!=s[i-k]:
            f=False
            break
        else:
            i+=1
    
    if f==True:
        print('YES')
    else:
        print('NO')
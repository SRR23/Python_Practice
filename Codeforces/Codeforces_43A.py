
t=int(input())
mp={}
while t>0:
    t-=1
    s=input()
    if s in mp:
        mp[s]+=1
    else:
        mp[s]=1

# find key, which value is maximum
print(max(mp,key=mp.get))
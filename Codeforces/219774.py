
x=input().split()
n=int(x[0])
m=int(x[-1])
a = list(map(int, input().strip().split()))[:n]
mp={}
for i in a:
    if i in mp:
        mp[i]+=1
    else:
        mp[i]=1


for i in range(1,m+1):
    if i in mp:
        print(mp[i])
    else:
        print(0)

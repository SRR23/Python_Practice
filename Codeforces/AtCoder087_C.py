n=int(input())

a = list(map(int, input().strip().split()))[:n]

mp={}
for i in a:
    if i in mp:
        mp[i]+=1
    else:
        mp[i]=1

cnt=0
for key,value in mp.items():
    if(value>key):
        cnt+=(value-key)
    elif(value<key):
        cnt+=value

print(cnt)
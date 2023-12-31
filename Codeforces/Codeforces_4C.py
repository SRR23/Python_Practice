
t=int(input())
mp={}
while t>0:
    t-=1
    s=input()
    if s in mp:
        mp[s]+=1
        print(f'{s}{mp[s]-1}')
    else:
        print('OK')
        mp[s]=1
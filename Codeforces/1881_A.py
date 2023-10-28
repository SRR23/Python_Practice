

t=int(input())
while t>0:
    t-=1
    x=input().split()
    n=int(x[0])
    m=int(x[-1])
    k=n
    sn=input()
    sm=input()
    # m+=1
    cnt=0
    while n<=m:
        n*=2
        cnt+=1
    
    if sn == sm:
        n//=2
        cnt-=1
        
    n/=k
    ans=""
    if(k>m):
        ans=sn
        cnt+=1

    for i in range(int(n)):
        ans+=sn
    
    f=-1
    if sm in ans:
        f=1
    
    if f==1:
        print(cnt)
    else:
        print(-1)
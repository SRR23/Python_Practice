
t=int(input())
while t>0:
    t-=1
    n=int(input())
    f,cnt=False,0
    while n>1:
        n=n/6 if n%6==0 else n*2
        if cnt>50:
            f=True
            break
        cnt+=1
    
    if f==True:
        print(-1)
    else:
        print(cnt)
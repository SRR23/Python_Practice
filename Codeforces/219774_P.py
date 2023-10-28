
n=int(input())
a=list(map(int,input().strip().split()))[:n]

cnt=0
while True:
    f=0
    for i in range(len(a)):
        if a[i]%2==1:
            f=1
    
    if(f==1):
        break
    else:
        cnt+=1
        for i in range(len(a)):
            a[i]//=2

print(cnt)
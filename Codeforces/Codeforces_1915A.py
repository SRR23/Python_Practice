t=int(input())
while t>0:
    t-=1
    x=list(map(int,input().strip().split()))[:3]
    a=x[0]
    b=x[1]
    c=x[2]
    a^=b
    a^=c
    print(a)
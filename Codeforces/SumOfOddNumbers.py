
# Sum of odd numbers between x and y

t=int(input())
while t>0:
    t-=1
    a=input().split()
    x=int(a[0])
    y=int(a[-1])
    mx=max(x,y)
    mn=min(x,y)
    tmp=0
    if mx%2==1:
        mx-=1
    if mn%2==1:
        tmp=mn
        mn-=1
    mx/=2
    mn/=2
    p=mx**2
    q=mn**2
    print(int(p-q-tmp))


def fun(a,b):
    sum=0
    for i in range(2,b+1,2):
        sum+=(a**i)
    return sum



x=input().split()
a=int(x[0])
b=int(x[-1])
ans=fun(a,b)
print(ans)
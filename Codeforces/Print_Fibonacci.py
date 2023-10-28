
a={}
def fibo(n):
    if n in a:
        return a[n]
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        ans=fibo(n-1)+fibo(n-2)
        a[n]=ans
        return ans


n=int(input())

for i in range(n):
    print(fibo(i),end=" ")

print()
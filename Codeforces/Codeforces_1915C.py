
from math import sqrt

def ok(n):
    return (round(sqrt(n))**2 == n)

t=int(input())
while t>0:
    t -= 1
    n = int(input())
    a = list(map(int, input().strip().split()))[:n]
    sum = 0
    for i in a:
        sum += i
    
    if ok(sum):
        print("YES")
    else:
        print("NO")
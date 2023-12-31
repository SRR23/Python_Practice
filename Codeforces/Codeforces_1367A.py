
t=int(input())
while t>0:
    t-=1
    s=input()
    print(s[0:len(s):2]+s[-1])
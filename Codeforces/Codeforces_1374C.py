
t=int(input())
while t>0:
    t-=1
    n,s=int(input()),input()
    while '()' in s:
        s=s.replace('()','')
    
    print(min(s.count('('), s.count(')')))
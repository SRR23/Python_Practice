
t=int(input())
while t>0:
    t-=1
    n=int(input())
    s=input()
    ans=''
    mp={'a':1, 'e':1}
    i=0
    ok=True
    while ok and i<n-1:
        if i+1<n and (s[n-1-i] in mp) and (s[n-1-(i+1)] not in mp):
            ans=ans+s[n-1-i]+s[n-1-(i+1)]+'.'
            i+=2
        elif i+2<n and (s[n-1-i] not in mp) and (s[n-1-(i+1)] in mp) and (s[n-1-(i+2)] not in mp):
            ans=ans+s[n-1-i]+s[n-1-(i+1)]+s[n-1-(i+2)]+'.'
            i+=3
        else:
            ok=False
    print(ans[-2::-1])
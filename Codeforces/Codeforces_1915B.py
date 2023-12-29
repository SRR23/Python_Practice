# Follow Codeforce_id xyyxyxxy 

t=int(input())
while t>0:
    t-=1
    a=input()
    b=input()
    c=input()
    
    x=ord(a[0])+ord(a[1])+ord(a[2])
    y=ord(b[0])+ord(b[1])+ord(b[2])
    z=ord(c[0])+ord(c[1])+ord(c[2])
    
    ans=(x+y+z)-ord('?')-198*3
    
    print(chr(-ans))
    
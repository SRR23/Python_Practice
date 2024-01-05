
import sys
input = lambda: sys.stdin.readline().rstrip()  # faster!
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')
 
for t in range(int(input())):
    s=input()
    s+='?'
    ans,p,i='','',0
    while i<len(s)-1:
        if s[i]==s[i+1]:
            ans+=s[i]*2
            i+=2
        else:
            ans+=s[i]
            i+=1
        
        if len(ans)%2!=0:
            p+=ans[0]
            ans=''
        else:
            ans=''
    
    print(''.join(sorted(set(p))))
    
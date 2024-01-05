
import sys
input = lambda: sys.stdin.readline().rstrip()  # faster!
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')
 
for t in range(int(input())):
    n,s=int(input()),input()
    ans,i=s[0],1
    while i<len(s):
        if ord(s[i])<=ord(s[i-1]):
            ans+=s[i]
            i+=1
        else:
            break
    
    if len(s)==1 or ord(s[0])<=ord(s[1]):
        print(s[0]+s[0])
    else:
        print(ans+ans[::-1])
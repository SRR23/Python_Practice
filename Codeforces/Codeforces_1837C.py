

import sys
input = lambda: sys.stdin.readline().rstrip()  # faster!
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')
 
for t in range(int(input())):
    s=list(input())
    s[0]='0' if s[0]=='?' else s[0]
    for i in range(1,len(s)):
        if s[i]=='?':
            s[i]=s[i-1]
    
    print(''.join(s))
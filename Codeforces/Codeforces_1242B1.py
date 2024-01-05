
import sys
input = lambda: sys.stdin.readline().rstrip()  # faster!
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')
 
for t in range(int(input())):
    n,s,s2=int(input()),input(),input()
    a=[]
    for i in range(n):
        if s[i]!=s2[i]:
            a.append(s[i]+s2[i])
    
    print('YES' if (len(a)==2 and a[0]==a[1]) or len(a)==0 else 'NO')

import sys, re
input = lambda: sys.stdin.readline().rstrip()  # faster!
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')
 

n,s=int(input()),input()
# Delete adjacent equal character
# s2=re.sub(r"(.)\1+", r"\1", s)
s+='A'
mx=p=0
for i,j in enumerate(s):
    if j.isupper():
        mx=max(mx,len(set(s[p:i:])))
        p=i+1
        
print(mx)
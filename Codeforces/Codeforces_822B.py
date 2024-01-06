import sys
input = lambda: sys.stdin.readline().rstrip()  # faster!
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')

def NotMatched(s1,s2):
    cnt=sum(1 for i in range(len(s1)) if s1[i]!=s2[i])
    return cnt

def position(s1,s2):
    a=[i+1 for i in range(len(s1)) if s1[i]!=s2[i]]
    return a
    
n,m=map(int,input().split())
s,t=input(),input()
mn,ln,ans=9999,len(s),''
for i in range(len(t)-ln+1):
    mn=min(mn,NotMatched(t[i:i+ln:],s))
    
for i in range(len(t)-ln+1):
    if NotMatched(t[i:i+ln:],s)==mn:
        ans=t[i:i+ln:]
        break

print(mn)
v=position(s,ans)
for i in v:
    print(i,end=" ")
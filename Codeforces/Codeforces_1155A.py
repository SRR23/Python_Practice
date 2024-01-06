import sys
input = lambda: sys.stdin.readline().rstrip()  # faster!
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')
 

n,s=int(input()),input()
if ''.join(sorted(s))==s:
    print('NO')
else:
    i=0
    while i<len(s)-1:
        if ord(s[i])>ord(s[i+1]):
            print('YES')
            print(i+1,i+2)
            break
        else:
            i+=1
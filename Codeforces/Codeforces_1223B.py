import sys
input = lambda: sys.stdin.readline().rstrip()  # faster!
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')
 
for t in range(int(input())):
    s,s2=input(),input()
    mp={x:1 for x in s}
    f=False
    for i in s2:
        if i in mp:
            f=True
            break
    print('YES' if f==True else 'NO')
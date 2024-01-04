
# https://codeforces.com/profile/gardengnome

import sys
input = lambda: sys.stdin.readline().rstrip()  # faster!
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')
 
for t in range(int(input())):
    n,s,s2=int(input()),input(),input().split()
    mx=p=0
    for i, j in enumerate(s):
        if j in s2:
            mx=max(mx,i-p)
            p=i
    print(mx)
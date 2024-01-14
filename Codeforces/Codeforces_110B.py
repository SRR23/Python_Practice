

import sys
input = lambda: sys.stdin.readline().rstrip()  # faster!
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')
 
n=int(input())
s='abcd'
for i in range(n):
    print(s[i%4],end="")
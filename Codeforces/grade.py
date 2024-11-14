import sys
input = lambda: sys.stdin.readline().rstrip()  # faster!
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')

for k in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    flag = 0
    array = []
    curr_win = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            curr_win+=1
        else:
            array.append(b[i]-a[i]+1)
    
    remain_win = ((n//2)+1)-curr_win
    
    if curr_win > remain_win:
        flag = 1
    
    array.sort()
    for i in array:
        if i > m:
            break
        m -= i
        remain_win -= 1
        if remain_win == 0:
            flag = 1
            break
    
    print("YES" if flag==1 else "NO")
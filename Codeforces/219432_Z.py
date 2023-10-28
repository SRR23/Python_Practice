
x=input().split()
a=int(x[0])
b=int(x[-1])
cnt=0
for i in range(0,a+1,1):
    for j in range(0,a+1,1):
        if(b>=(i+j)and(b-(i+j))<=a):
            cnt+=1

print(cnt)
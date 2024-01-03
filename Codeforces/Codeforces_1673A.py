

for t in range(int(input())):
    s=input()
    a=[ord(s[i])-96 for i in range(len(s))]
    p,A,B=sum(a),sum(a)-a[0]*2,sum(a)-a[-1]*2
    print(f'Alice {p}' if len(s)%2==0 else (f'Alice {max(A,B)}' if len(a)>1 else f'Bob {a[0]}'))
    
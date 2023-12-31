
n=int(input())
s=input()
a,b=s.count('A'),s.count('D')
ans="Anton" if a>b else ("Danik" if b>a else "Friendship")
print(ans)
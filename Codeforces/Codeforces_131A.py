
s=input()
ans=s.swapcase() if s.isupper() or (s[0].islower() and s[1::].isupper()) or (len(s)==1 and s[0].islower()) else s
print(ans)
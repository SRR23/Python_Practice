
def reverse(str):
    string=""
    for i in range(len(str)-1,-1,-1):
        string+=str[i]
    return string


inp=input()
t=int(inp)
k=1
while k<=t:
    string=input()
    ans=reverse(string)
    for i in range(len(ans)):
        print(ans[i],end=" ")
    
    print()
    k+=1

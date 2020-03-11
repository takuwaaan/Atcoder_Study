def digit10(x):
    dten = 0
    while(x>0):
        dten+=int(x%10)
        x/=10
    return dten

n = int(input())
if n%digit10(n)==0:
    print("Yes")
else:
    print("No")
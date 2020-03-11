n=int(input())
s=input()
if n%2 != 0:
    print("No")
else:
    f=True
    for i in range(n//2):
        if s[i] != s[i+n//2]:
            f=False
    if f:
        print("Yes")
    else:
        print("No")


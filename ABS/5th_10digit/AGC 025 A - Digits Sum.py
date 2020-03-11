def digit_10(n):
    dten = 0
    while(n>0):
        dten+=int(n%10)
        n/=10
    return dten

n = int(input())
l = []
for a in range(1,n):
    l.append(digit_10(a)+digit_10(n-a))
print(min(l))
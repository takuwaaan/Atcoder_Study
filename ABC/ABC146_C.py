a,b,x = map(int,input().split())

h=10**9
m=(10**9)//2
l=0

if a+b>x:
    print(0)
elif x>=a*(10**9)+b*10:
    print(10**9)
else:
    for i in range(50):
        if x>=a*m+b*len(str(m)):
            l=m
            m=(h+m)//2
        else:
            h=m
            m=(m+l)//2
    print(m)
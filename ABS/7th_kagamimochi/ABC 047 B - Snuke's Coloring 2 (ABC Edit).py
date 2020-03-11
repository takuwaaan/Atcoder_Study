w,h,n = map(int,input().split())
xya = []
for i in range(n):
    array = list(map(int, input().strip().split()))
    xya.append(array)

xl1 =[0]
xl2 =[w]
yl3 =[0]
yl4 =[h]
for i in range(n):
    if xya[i][2]==1:
        xl1.append(xya[i][0])
    elif xya[i][2]==2:
        xl2.append(xya[i][0])
    elif xya[i][2]==3:
        yl3.append(xya[i][1])
    elif xya[i][2]==4:
        yl4.append(xya[i][1])
s1=min(xl2)-max(xl1)
s2=min(yl4)-max(yl3)

if s1>0 and s2>0:
    s = s1*s2
    print(s)
else:
    print(0)
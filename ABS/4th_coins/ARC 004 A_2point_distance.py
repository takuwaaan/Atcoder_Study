import math

def dis_xy(x1,y1,x2,y2):
    dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return dis

n = int(input())
x = [0]*(n)
y = [0]*(n)
for i in range(n):
    x[i],y[i] = map(int,input().split())
d = []
for i in range(n):
    for j in range(n):
        d.append(dis_xy(x[i],y[i],x[j],y[j]))

print(max(d))
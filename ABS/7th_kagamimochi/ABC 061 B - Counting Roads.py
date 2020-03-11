n,m = map(int,input().split())
x = [0]*m
y = [0]*m
for i in range(m):
    x[i],y[i] = map(int,input().split())
l = [0]*n
for i in range(m):
    l[x[i]-1] += 1
    l[y[i]-1] += 1
for i in range(n):
    print(l[i])
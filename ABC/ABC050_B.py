n = int(input())
t = list(map(int,input().split()))
m = int(input())
p = [0]*m
x = [0]*m
for i in range(m):
    p[i],x[i] = map(int,input().split())

for i in range(m):
    s=[]
    for j in range(n):
        s.append(t[j])
    s[p[i]-1] = x[i]
    print(sum(s))

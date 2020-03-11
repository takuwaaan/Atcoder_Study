n,x = map(int,input().split())
m = []
for i in range(n):
    m.append(int(input()))
print(n+int((x-sum(m))/min(m)))
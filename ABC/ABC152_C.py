n = int(input())
p = list(map(int,input().split()))
mtmp = p[0]
ans = 0
for i in range(0,n):
    if mtmp>=p[i]:
        mtmp=p[i]
        ans+=1
print(ans)
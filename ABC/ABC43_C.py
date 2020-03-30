N = int(input())
a = list(map(int,input().split()))
a.sort()
c = round(sum(a)/N)
ans = 0
for i in range(N):
    ans += (a[i]-c)**2
print(ans)
#証明。。。？
n,k=map(int,input().split())
h=list(map(int,input().split()))
h.sort(reverse=True)
ans = 0
if k>=n:
    ans = 0
else:
    for i in range(k):
        h[i] = 0
    ans = sum(h)
print(ans)
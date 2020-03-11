n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))
for i,ave in enumerate(h):
    h[i] = abs(a-(t-h[i]*0.006))
ans = h.index(min(h))+1
print(ans)
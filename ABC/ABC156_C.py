N = int(input())
X = [int(x) for x in input().split()]

center = round((sum(X) / N), 0)

ans = 0
for i in range(N):
    ans += (X[i] - int(center)) ** 2

print(ans)

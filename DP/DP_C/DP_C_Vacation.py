N = int(input())
a = [[0] * 3] * N
for i in range(N):
    a[i][0], a[i][1], a[i][2] = map(int, input().split())

dp = [[0] * 3] * (N + 1)
print(dp)

for i in range(N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            print(dp[i][j], a[i][k])
            dp[i][k] = max(dp[i + 1][k], (dp[i][j] + a[i][k]))
print(dp)

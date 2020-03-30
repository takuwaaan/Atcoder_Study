N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]
a_s = set(a)
mod = 1000000007

dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    if i in a_s:
        continue
    elif i >= 2:
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    else:
        dp[i] = (dp[i - 1]) % mod
print(dp[-1])

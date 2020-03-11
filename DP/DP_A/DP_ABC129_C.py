#https://atcoder.jp/contests/abc129/tasks/abc129_c
#入力の差でTLE

n, m = [int(x) for x in input().split()]
a = set(int(input()) for _ in range(m))
"""
下記で実装するとTLE
n, m = map(int, input().split())
a = []
mod = 10 ** 9 + 7
for _ in range(m):
    a.append(int(input()))
"""
mod = 10 ** 9 + 7

dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    #https://tkkm.tokyo/post-173/#outline__1_1
    #この探索のときにlistかsetかで変わってるかも
    if i in a:
        continue
    if i >= 2:
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    else:
        dp[i] = dp[i - 1]
print(dp)
print(dp[-1])

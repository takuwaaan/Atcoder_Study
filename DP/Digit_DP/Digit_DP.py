# https://qiita.com/pinokions009/items/1e98252718eeeeb5c9ab

N = input()
l = len(N)
dp = [[[0] * 2 for _ in range(2)] for _ in range(100)]
dp[0][0][0] = 1

for i in range(l):
    for smaller in range(2):
        for j in range(2):
            for x in range(9 if smaller else int(N[i])):
                dp[i + 1][smaller | (x < int(N[i]))][j | (x == 3)] += dp[i][smaller][j]
print(dp)
print(dp[l][0][1] + dp[l][1][1])

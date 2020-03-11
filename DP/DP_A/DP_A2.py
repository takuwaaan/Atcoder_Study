N=int(input())
h=[int(i) for i in input().split()]

#DPテーブル＆最小化問題なのでINFに初期化
dp = [float("inf")]*N
#初期条件
dp[0] = 0
#ループ
for i in range(N):
    dp[i] = min(dp[i],dp[i-1]+abs(h[i]-h[i-1]))
    if i>1:
        dp[i] = min(dp[i],dp[i-2]+abs(h[i]-h[i-2]))

print(dp[-1])

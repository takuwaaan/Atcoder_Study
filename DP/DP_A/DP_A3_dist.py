#配るDP
#DPテーブル＆最小化問題なのでINFに初期化
h = [0]*100010
dp = [float("inf")]*100010

N=int(input())
H=list(map(int,input().split()))

for i in range(N):
    h[i] = H[i]

#初期条件
dp[0] = 0
#ループ
for i in range(N):
    dp[i+1] = min(dp[i+1],dp[i]+abs(h[i]-h[i+1]))
    dp[i+2] = min(dp[i+2],dp[i]+abs(h[i]-h[i+2]))
print(dp[N-1])

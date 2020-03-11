#メモ化再帰
#入力
h = [0]*100010
dp = [float("inf")]*100010

def rec(i):
    #DPの値が更新されていたらそのままリターン
    if dp[i]<float("inf"):
        return dp[i]
    if i==0:
        return 0
    res = float("inf")
    res = min(res,rec(i-1)+abs(h[i]-h[i-1]))
    if i>1:
        res = min(res, rec(i - 2) + abs(h[i] - h[i - 2]))
    dp[i]=res
    return dp[i]

#入力
N=int(input())
H=list(map(int,input().split()))
for i in range(N):
    h[i] = H[i]

print(rec(N-1))
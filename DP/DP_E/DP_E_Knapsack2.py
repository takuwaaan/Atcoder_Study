#https://atcoder.jp/contests/dp/submissions/7819099
N, W = [int(i) for i in input().split()]
WV = [[int(i) for i in input().split()] for j in range(N)]

import numpy as np
max_value = np.sum(np.array(WV), axis=0)[1]

# dp[v]: 価値vを達成するのに必要な重さの最小値
dp = np.full(max_value + 1, W + 1, dtype='int64')
print(max_value)
print(dp)
dp[0] = 0
print(dp)
for w, v in WV:
    # 価値i(0 <= i <= max_value - v)のときの重さの最小値に対し
    # 次の荷物を入れて、価値i+vのときの重さの最小値を更新
    print(w,v,dp[:-v]+w)
    print(dp[v:])
    np.minimum(dp[:-v] + w, dp[v:], out=dp[v:])
    print(dp)
print(np.max(np.where(dp <= W)))

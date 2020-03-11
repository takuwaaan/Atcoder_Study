#https://qiita.com/drken/items/dc53c683d6de8aeacf5a

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
H = [int(x) for x in input().split()]

dp = [0] * N
dp[1] = abs(H[1]-H[0])
#for i in range(2,N):
#    dp[i] = min(dp[i-1] + abs(H[i]-H[i-1]), dp[i-2] + abs(H[i]-H[i-2]))
for i in range(2,N):
    dp[i] = min(dp[i-k] + abs(H[i]-H[i-k]) for k in [1,2])

answer = dp[-1]
print(answer)


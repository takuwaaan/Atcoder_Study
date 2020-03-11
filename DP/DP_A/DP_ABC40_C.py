# https://atcoder.jp/contests/abc040/tasks/abc040_c

n = int(input())
a = list(map(int, input().split()))

count = 0
dp = []

# 0
dp.append(0)
# 0, 50
dp.append(abs(a[0] - a[1]))

for i in range(1,n-1):
    dp.append(min((dp[i] + abs(a[i+1] - a[i])), (dp[i-1] + abs(a[i+1] - a[i-1]))))
print(dp[-1])

# 0, 50 ,30
#dp.append(max((dp[1] + abs(a[2]-a[1])),(dp[0] + abs(a[2]-a[0]))))
# 0, 50, 30, 10
#dp.append(max((dp[2] + abs(a[3]-a[2])),(dp[1] + abs(a[3]-a[1]))))

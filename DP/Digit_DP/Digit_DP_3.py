#http://zehnpaard.hatenablog.com/entry/2018/06/24/215607
#３がつく数の総数を求める

from itertools import product
from collections import defaultdict

a = input()
n = len(a)

dp = defaultdict(int)
dp[0, 0, 0] = 1

for i, less, has3 in product(range(n), (0,1), (0,1)):
    max_d = 9 if less else int(a[i])
    for d in range(max_d+1):
        less_ = less or d < max_d
        has3_ = has3 or d == 3
        dp[i + 1, less_, has3_] += dp[i, less, has3]

print(sum(dp[n, less, 1] for less in (0, 1)))
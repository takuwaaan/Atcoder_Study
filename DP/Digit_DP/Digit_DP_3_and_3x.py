from itertools import product
from collections import defaultdict

a = input()
n = len(a)

dp = defaultdict(int)
dp[0, 0, 0, 0] = 1
;
for i, less, has3, mod3 in product(range(n), (0,1), (0,1), range(3)):
    max_d = 9 if less else int(a[i])
    for d in range(max_d+1):
        less_ = less or d < max_d
        has3_ = has3 or d == 3
        mod3_ = (mod3 + d) % 3
        dp[i + 1, less_, has3_, mod3_] += dp[i, less, has3, mod3]

criteria = ((n, less, has3, mod3) for less, has3, mod3
                                  in product((0, 1), (0,1), range(3))
                                  if has3 or mod3==0)

print(sum(dp[c] for c in criteria))
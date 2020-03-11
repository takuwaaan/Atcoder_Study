# 参考：https://atcoder.jp/contests/dp/submissions/5316523

n, W = map(int, input().split())
w, v = [0] * n, [0] * n
for i in range(n):
    w[i], v[i] = map(int, input().split())

import numpy as np

ndp = np.zeros(W + 1, dtype=np.int64)

# print(ndp)

for w, v in zip(w, v):
    #    print(w,v,ndp[:-w] + v)
    #    print(w,v,ndp[w:])
    np.maximum(ndp[:-w] + v, ndp[w:], out=ndp[w:])
#    print(w,v,ndp)

print(ndp[-1])

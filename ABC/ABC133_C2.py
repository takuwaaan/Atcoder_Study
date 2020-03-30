import sys

L, R = map(int, input().split())
mod = 2019
ans = []
if R-L > 3000:
    print(0)
    sys.exit()
elif R-L <= 3000:
    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            tmp = (i * j) % mod
            ans.append(tmp)
print(min(ans))

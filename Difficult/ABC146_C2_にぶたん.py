# 参考：https://atcoder.jp/contests/abc146/submissions/8610074
# にぶたん

def N_max(mid):
    return A * mid + B * len(str(mid)) <= X


A, B, X = map(int, input().split())
OK = 0
NG = 10 ** 18
while abs(OK - NG) > 1:
    mid = (OK + NG) // 2
    if N_max(mid):
        OK = mid
    else:
        NG = mid

print(OK if OK <= 10**9 else 10**9)

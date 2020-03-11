X, Y = map(int, input().split())
mod = 10 ** 9 + 7


# nCr フェルマーの小定理より（ABC156D参照）
def comb_mod(n, r, mod):
    num = 1
    den = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod
    den_r = pow(den, mod - 2, mod)
    return (num * den_r) % mod


# n+2m=X,2n+m=Yより
n = (2 * Y - X) // 3
m = (2 * X - Y) // 3

# 3の倍数以外は0
# (0,6)など、n<0 or m<0のときも0
if (X + Y) % 3 != 0 or n < 0 or m < 0:
    print(0)
else:
    print(comb_mod(n + m, n, mod))

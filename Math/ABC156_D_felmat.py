n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
#2 ** n は入力が10**9となった場合にオーバーフロー
n_max = pow(2, n, mod) - 1


def comb_mod(n, r, mod):
    num = 1
    den = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod
    den_r = pow(den, mod - 2, mod)
    return (num * den_r) % mod


ans = (n_max - comb_mod(n, a, mod) - comb_mod(n, b, mod)) % mod
print(ans)

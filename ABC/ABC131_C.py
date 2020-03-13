# 最大公約数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


A, B, C, D = map(int, input().split())
l = lcm(C, D)
div_C = B // C - (A - 1) // C
div_D = B // D - (A - 1) // D
div_lcm = B // l - (A - 1) // l
div = div_C + div_D - div_lcm
ans = (B - A + 1) - div
print(ans)

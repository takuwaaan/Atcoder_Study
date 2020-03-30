# 最大公約数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


A, B, C, D = map(int, input().split())
fC = B // C - (A - 1) // C
fD = B // D - (A - 1) // D
l = lcm(C, D)
fCD = B // l - (A - 1) // l
print(B - A + 1 - (fC + fD - fCD))

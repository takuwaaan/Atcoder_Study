a = 6
b = 10

# 最大公約数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(a, b))

# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(a, b))

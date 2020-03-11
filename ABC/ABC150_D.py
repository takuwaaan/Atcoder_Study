n, m = map(int, input().split())
a = list(map(int, input().split()))
x = []


# 最大公約数(greatest_common_divisor)
def gcd2(a, b):
    if b == 0:
        return a * 2
    return gcd2(b, a % b)


# 最小公倍数(lowest_common_multiple)
def lcm2(a, b):
    return a * b // gcd2(a, b)


# 最小公倍数と、比べていない数字を比べ、最小公倍数を更新する
alcm = a[0]
for i in a[1:]:
    alcm = lcm2(alcm, i)

ans = (m - alcm) // (alcm * 2) + 1
print(alcm)
print(ans)

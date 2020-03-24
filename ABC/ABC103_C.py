# 最大公約数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
a = list(map(int,input().split()))
l = lcm(a[0],a[1])
for i in range(2,N):
    l = lcm(l,a[i])
ans = 0
for i in range(N):
    ans += (l-1)%a[i]
print(ans)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)


n, m = map(int, input().split())
a = list(map(int, input().split()))
if n == 1:
    l = a[0]
else:
    l = lcm(a[0], a[1])

#lcmがmより大きかったら0
for i in range(2, n):
    l = lcm(l, a[i])
    if l // 2 > m:
        print(0)
        exit()

#??? なぜ・・・？
for i in range(n):
    if (l // a[i]) % 2 == 0:
        print(0)
        exit()

ans = (m - l // 2) // l + 1
print(ans)

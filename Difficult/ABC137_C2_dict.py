from collections import defaultdict

n = int(input())
dct = defaultdict(int)

for i in range(n):
    s = input()
    sorted_s = "".join(sorted(s))
    dct[sorted_s] += 1

print(dct)
ans = 0
for k, v in dct.items():
    ans += v * (v - 1) // 2

print(ans)
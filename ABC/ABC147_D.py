#pypyだとREになるので注意
import numpy as np

n = int(input())
s = input().split()
a = []
for i in range(n):
    a.append(int(s[i]))
arr = np.array(a)
# arr = np.array([int(i) for i in input().split()])

mod = 10 ** 9 + 7
ans = 0

for i in range(60):
    #arrについて2進数を右へ論理シフトした値になる？
    c1 = np.count_nonzero(arr & 1)
    ans += 2 ** i * c1 * (n - c1)
    arr >>= 1

print(ans % mod)

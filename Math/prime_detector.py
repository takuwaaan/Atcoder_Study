"""
いろんな素数判定方法
https://qiita.com/srtk86/items/874639e361917e5016d4
"""

"""

n = 1213
for p in range(2, n):
    if n % p == 0:
        print(str(n) + ' is composite.')
        break
print(str(n) + ' is PRIME!!')

"""

import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True
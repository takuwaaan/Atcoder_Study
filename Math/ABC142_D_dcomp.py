import math


# 公約数列挙
# 重複する約数は1つにまとまるので注意
def make_common_divisors(x1, x2):
    cd = [1]
    for i in range(2, min(x1, x2) + 1):
        if x1 % i == 0 and x2 % i == 0:
            cd.append(i)
    return cd


# nを素因数分解したリストを返す
def decomposition_prime(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(int(n))
    return table

# 引数nが素数かどうかを判定
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


A, B = map(int, input().split())
Ap = set(decomposition_prime(A))
Bp = set(decomposition_prime(B))
print(len(Ap & Bp)+1)
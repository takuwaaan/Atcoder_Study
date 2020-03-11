
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

A, B = map(int, input().split())
Ap = set(decomposition_prime(A))
Bp = set(decomposition_prime(B))
print(len(Ap & Bp)+1)
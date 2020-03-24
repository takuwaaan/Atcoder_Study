N, M = map(int, input().split())
if N > 0 or M > 0:
    a = N - 1
    b = M - 1
else:
    a = 0
    b = 0
print((a * (a + 1)) // 2 + (b * (b + 1)) // 2)

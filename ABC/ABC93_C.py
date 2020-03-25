L = list(map(int, input().split()))
L.sort()
d1 = L[-1] - L[-2]
d2 = L[-1] - d1 - L[0]
if d2 % 2 == 0:
    print(d1 + d2 // 2)
else:
    print(d1 + d2 // 2 + 2)

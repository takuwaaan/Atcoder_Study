A, B = map(int, input().split())
K = (A ** 2 - B ** 2) / (2 * (A - B))
if K % 1 != 0:
    print("IMPOSSIBLE")
else:
    print(int(K))
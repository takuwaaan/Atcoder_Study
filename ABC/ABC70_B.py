A, B, C, D = map(int, input().split())
d = min(B,D) - max(A,C)
if d < 0:
    print(0)
else:
    print(d)

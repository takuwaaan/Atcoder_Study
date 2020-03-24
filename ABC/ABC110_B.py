N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort()
y.sort()
f = True
for i in range(X + 1, Y + 1):
    if x[-1] < i <= y[0]:
        f = False
        break
if f:
    print("War")
else:
    print("No War")
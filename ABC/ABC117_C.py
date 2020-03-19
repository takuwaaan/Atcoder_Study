N, M = map(int, input().split())
X = list(map(int, input().split()))
if N >= M:
    print(0)
else:
    X.sort()
    X_div = [0] * (M - 1)
    for i in range(1, M):
        X_div[i - 1] = X[i] - X[i - 1]
    X_div.sort(reverse=True)
    m = 0
    for i in range(N - 1):
        m += X_div[i]
    print(X[-1] - X[0] - m)

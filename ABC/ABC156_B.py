N, K = map(int, input().split())


def Digit(X, n):
    X_dumy = X
    out = ''
    while X_dumy > 0:
        out = str(X_dumy % n) + out
        X_dumy = int(X_dumy / n)
    return out


leng = str(Digit(N, K))
print(len(leng))

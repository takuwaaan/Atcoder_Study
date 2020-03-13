N, D = map(int, input().split())
c = D * 2 + 1
if N % c == 0:
    print(N // c)
else:
    print(N // c + 1)

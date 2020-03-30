N, M = map(int, input().split())

if (M - N * 2) >= 0:
    print(N + (M - N * 2)//4)
else:
    print(M//2)

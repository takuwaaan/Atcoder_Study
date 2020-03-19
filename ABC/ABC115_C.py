N, K = map(int, input().split())
h = [0] * N
for i in range(N):
    h[i] = int(input())
h.sort()
deco = 10 ** 9
for i in range(N - K + 1):
    if h[i + K - 1] - h[i] < deco:
        deco = h[i + K - 1] - h[i]
print(deco)

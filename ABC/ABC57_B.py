N, M = map(int, input().split())
a = [0] * N
b = [0] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())
c = [0] * M
d = [0] * M
for i in range(M):
    c[i], d[i] = map(int, input().split())

ans = []
for i in range(N):
    for j in range(M):
        tmp = abs(a[i] - c[j]) + abs(b[i] - d[j])
        ans.append(tmp)
    print(ans.index(min(ans)) + 1)
    ans = []

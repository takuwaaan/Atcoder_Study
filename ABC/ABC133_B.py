import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]

ans = 0
tmp = 0
s = 1.5
for i in range(N):
    for k in range(N):
        if i == k:
            continue
        else:
            for j in range(D):
                tmp += (X[i][j] - X[k][j]) ** 2
                s = math.sqrt(tmp)
        if s % 1 == 0:
            ans += 1
        s = 0
        tmp = 0
print(ans//2)

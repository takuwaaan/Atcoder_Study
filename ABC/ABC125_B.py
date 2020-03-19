N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
XY = [0] * N
ans = 0
for i in range(N):
    XY[i] = V[i]-C[i]
    if XY[i] >= 0:
        ans += XY[i]
print(ans)
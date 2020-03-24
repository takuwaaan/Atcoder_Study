N, T = map(int, input().split())
ans = 10 ** 4
root = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if root[i][1] > T:
        continue
    else:
        ans = min(ans, root[i][0])

print("TLE" if ans == 10 ** 4 else ans)

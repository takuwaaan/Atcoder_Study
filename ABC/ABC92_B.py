N = int(input())
D, X = map(int, input().split())
ans = 0
for i in range(N):
    A = int(input())
    for _ in range(1, D + 1, A):
        ans += 1
print(ans + X)

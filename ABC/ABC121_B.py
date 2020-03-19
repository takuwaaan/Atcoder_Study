N, M, C = map(int, input().split())
B = list(map(int, input().split()))
count = C
ans = 0
for _ in range(N):
    A = list(map(int, input().split()))
    for i in range(M):
        count += A[i] * B[i]
    if count > 0:
        ans += 1
    count = C
print(ans)

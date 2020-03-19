N, M = map(int, input().split())
like = [0] * (M + 1)
for _ in range(N):
    KA = list(map(int, input().split()))
    for i in range(1, len(KA)):
        like[KA[i]] += 1
like.sort(reverse=True)
ans = 0
for i in range(M + 1):
    if like[i] == N:
        ans += 1
    else:
        break
print(ans)

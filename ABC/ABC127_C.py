N, M = map(int, input().split())
key = [0] * (N + 1)
tmp_R = 10 ** 5
tmp_L = 1
for _ in range(M):
    L, R = map(int, input().split())
    if L >= tmp_L:
        tmp_L = L
    if R <= tmp_R:
        tmp_R = R
ans = tmp_R - tmp_L + 1
if ans < 0:
    print(0)
else:
    print(ans)

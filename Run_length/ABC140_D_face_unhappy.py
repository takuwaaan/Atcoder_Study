N, K = map(int, input().split())
S = list(input())
count = 0
f = True
for i in range(N - 1):
    if S[i] == S[i + 1]:
        count += 1
ans = count + 2 * K
if ans < N - 1:
    print(ans)
else:
    print(N - 1)

N, M = map(int, input().split())
s = [0] * M
c = [0] * M
for i in range(M):
    s[i], c[i] = map(int, input().split())

w = ""
ans = [-1] * N
f = True

if N == 1 and M == 0:
    print(0)
elif N == 1:
    for i in range(M):
        if ans[s[i] - 1] != -1:
            if ans[s[i] - 1] != c[i]:
                f = False
                break
        ans[s[i] - 1] = c[i]
    if f:
        if ans[0] == -1:
            ans[0] = 1
        for i in range(1, N):
            if ans[i] == -1:
                ans[i] = 0
        for i in range(N):
            w += str(ans[i])
        print(int(w))
    if not f:
        print(-1)

elif N == 2 or N ==3:
    for i in range(M):
        if s[i] == 1 and c[i] == 0:
            f = False
            break
        if ans[s[i] - 1] != -1:
            if ans[s[i] - 1] != c[i]:
                f = False
                break
        ans[s[i] - 1] = c[i]
    if f:
        if ans[0] == -1:
            ans[0] = 1
        for i in range(1, N):
            if ans[i] == -1:
                ans[i] = 0
        for i in range(N):
            w += str(ans[i])
        print(int(w))
    if not f:
        print(-1)

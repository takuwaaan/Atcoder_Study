N, Q = map(int, input().split())
S = input()
AC = [0] * (N)
for i in range(1, N):
    if S[i] == "C" and S[i - 1] == "A":
        AC[i] = AC[i - 1] + 1
    else:
        AC[i] = AC[i - 1]
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(AC[r] - AC[l])

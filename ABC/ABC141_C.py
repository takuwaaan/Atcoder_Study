N, K, Q = map(int, input().split())
S = [K - Q] * N
for i in range(Q):
    A = int(input())
    S[A - 1] += 1
for i in range(N):
    if S[i] > 0:
        print("Yes")
    else:
        print("No")

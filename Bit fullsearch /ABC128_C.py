#https://atcoder.jp/contests/abc128/submissions/5638298

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = [list(map(int, input().split()))[1:] for i in range(M)]

P = list(map(int, input().split()))
ANS = 0

for i in range(1 << N):
    print(i)
    for m in range(M):
        ANS2 = 0
        for s in S[m]:
            if i & (1 << (s - 1)) != 0:
                ANS2 += 1

        print(i,ANS2)
        if ANS2 % 2 != P[m]:
            break

    else:
        ANS += 1

print(ANS)


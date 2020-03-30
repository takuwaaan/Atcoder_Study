#https://atcoder.jp/contests/abc128/submissions/5638298

#https://sepat.hatenablog.com/entry/2019/05/30/231217

N, M = map(int, input().split())
S = [list(map(int, input().split()))[1:] for i in range(M)]

P = list(map(int, input().split()))
ans = 0

for i in range(2**N):
    judge = True
    for m in range(M):
        cnt = 0

        for s in S[m]:
            if i & (1 << (s - 1)) != 0:
                cnt += 1
        if cnt % 2 != P[m]:
            judge = False
    if judge:
        ans += 1

print(ans)


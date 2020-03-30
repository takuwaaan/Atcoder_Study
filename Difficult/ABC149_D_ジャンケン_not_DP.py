# https://atcoder.jp/contests/abc149/submissions/9213312

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

win_pt = {"r": P, "s": R, "p": S}
pt = [0] * N

for i, t in enumerate(T):
    if i < K:
        pt[i] = win_pt[t]
    elif i >= K and (T[i - K] != T[i] or pt[i - K] == 0):
        pt[i] = win_pt[t]
print(sum(pt))

# 参考：https://atcoder.jp/contests/abc146/submissions/10412733

from collections import deque

N = int(input())
# グラフ準備
graph = [[] for _ in range(N + 1)]
seq = []

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    seq.append(b)

# BFS

q = deque([1])
color = [0] * (N + 1)

while q:
    checking_parent = q.popleft()
    parent_color = color[checking_parent]
    c = 1
    for child in graph[checking_parent]:
        if c == parent_color:
            c += 1
        # 使用したcolorをchildの色として格納する
        color[child] = c
        c += 1
        # childを探索候補へ追加
        q.append(child)

print(max(color))
for i in range(N - 1):
    print(color[seq[i]])

#https://atcoder.jp/contests/abc138/submissions/7003989

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

# 遅延評価で加えてあげるだけ

N, Q = map(int, input().split())
AB = [[int(x) for x in input().split()] for _ in range(N - 1)]
PX = [[int(x) for x in input().split()] for _ in range(Q)]

print(AB)
print(PX)
graph = [[] for _ in range(N + 1)]
for a, b in AB:
    graph[a].append(b)
    graph[b].append(a)
print("graph:", graph)

value = [0] * (N + 1)
for p, x in PX:
    value[p] += x
print("value:", value)
q = [(1, 0)]
print("***loop***")
while q:
    x, parent = q.pop()
    print("x:", x, "parent:", parent)
    value[x] += value[parent]
    print("value:",value)
    for y in graph[x]:
        if y == parent:
            continue
        q.append((y, x))
    print("q:",q)

answer = ' '.join(map(str, value[1:]))
print(answer)
print(*value[1:])#同じだけど少し遅い

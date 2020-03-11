#https://atcoder.jp/contests/abc146/submissions/10412733

#import sys

#sys.setrecursionlimit(10 ** 7)
#read = sys.stdin.buffer.read
#inp = sys.stdin.buffer.readline

#def inpS(): return inp().rstrip().decode()

#readlines = sys.stdin.buffer.readlines

from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
nextV = []

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    nextV.append(b)
print("graph:",graph)
print("for answer:",nextV)

q = deque([1])  # 頂点1から幅優先探索
color = [0] * (N + 1)
print("Used color:",color)
print("*****First loop*****")
while q:
    print(q)
    v = q.popleft()
    print("pop(checking parent_node):",v)
    parentC = color[v]
    c = 1
    for child in graph[v]:
        print("checking child_node:",child)
        if c == parentC:  # 親と同じ色だったら次の色へスキップ
            c += 1
        color[child] = c  # 使用した色を保持
        c += 1  # 次の色へスキップ
        q.append(child)
        print("color_add:",color)
    print("*******whileループ*******")

print(max(color))
for b in nextV:
    print(color[b])
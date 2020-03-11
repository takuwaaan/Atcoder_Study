R, C = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))

#listの形に合わせてる
sy -= 1
sx -= 1
gy -= 1
gx -= 1

#迷路の作成
graph = []
for i in range(R):
    row = input()
    graph.append(list(row))

print(graph)
#迷路と同じ形の何もない空間を作成
costs = []
for i in range(R):
    costs.append([None]*C)
print(costs)

costs[sy][sx] = 0
q = [[sy, sx]]

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

while len(q) != 0:
    y, x = q.pop(0)

    for i in range(4):
        t = y + di[i]
        u = x + dj[i]
        if graph[t][u] == '#':
            continue
        if costs[t][u] is not None:
            continue
        costs[t][u] = costs[y][x] + 1
        q.append([t, u])

for ci in costs:
    print(ci)

print(costs[gy][gx])

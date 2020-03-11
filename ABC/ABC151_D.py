H, W = list(map(int, input().split()))

#迷路の作成
graph = [list(input()) for i in range(H)]
#迷路と同じ形の何もない空間を作成
ans = 0
for i in range(H):
    for j in range(W):
        costs = []
        for l in range(H):
            costs.append([-1] * W)
        sy = i
        sx = j
        if graph[sy][sx] == "#":
            continue
        costs[sy][sx] = 0
        q = [[sy, sx]]
        #移動方向
        di = [1, -1, 0, 0]
        dj = [0, 0, -1, 1]

        while len(q) != 0:
            y, x = q.pop(0)

            for k in range(4):
                t = y + di[k]
                u = x + dj[k]
                if not (0<=t<H and 0<=u<W):
                    continue
                if graph[t][u] == '#':
                    continue
                if costs[t][u] != -1:
                    continue
                costs[t][u] = costs[y][x] + 1
                q.append([t, u])
        #ここはちゃんと書こう。。。
        ans = max(ans, max([max(d) for d in costs]))
print(ans)
H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
a = [[0] * (W + 2) for _ in range(H + 2)]
for i in range(H):
    for j in range(W):
        tmp_i = i + 1
        tmp_j = j + 1

        if s[i][j] == "#":
            a[tmp_i + 1][tmp_j] += 1
            a[tmp_i - 1][tmp_j] += 1
            a[tmp_i][tmp_j + 1] += 1
            a[tmp_i][tmp_j - 1] += 1
            a[tmp_i + 1][tmp_j + 1] += 1
            a[tmp_i + 1][tmp_j - 1] += 1
            a[tmp_i - 1][tmp_j + 1] += 1
            a[tmp_i - 1][tmp_j - 1] += 1
for i in range(H):
    for j in range(W):
        tmp_i = i + 1
        tmp_j = j + 1
        if s[i][j] == "#":
            a[tmp_i][tmp_j] = "#"
ans = []
for i in range(1,H+1):
    for j in range(1,W+1):
        ans.append(str(a[i][j]))
    print("".join(ans))
    ans = []

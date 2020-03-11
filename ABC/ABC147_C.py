n = int(input())
xy = []
for i in range(n):
    a = int(input())
    xy.append([])
    for j in range(a):
        tmp = list(map(int, input().split()))
        xy[i].append(tmp)
# bit全探索
# 範囲
ans = 0
s = 0
for i in range(2 ** n):
    # 判断用のリストを準備
    judge = []
    # 探索
    for j in range(n):
        if (i >> j) & 1:
            judge.append(1)
        else:
            judge.append(0)

    count = 0
    tmp_j = True
    for l in range(n):
        count = 1
        if judge[l] == 1:
            for a in range(len(xy[l])):
                if judge[xy[l][a][0] - 1] == xy[l][a][1]:
                    count = 1
                if judge[xy[l][a][0] - 1] != xy[l][a][1]:
                    count = 0
                    tmp_j = False
                    break
        if tmp_j == False:
            break

    if count == 1:
        s = sum(judge)
    if ans <= s:
        ans = s
print(ans)

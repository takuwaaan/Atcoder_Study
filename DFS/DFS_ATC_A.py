#フレームワーク
"""
探索スタート地点を「探索候補スタック」に積む
while スタックが空っぽになるまで
    スタックから次の探索地点を1つ取り出す（pop）
    「探索済みリスト」に取り出した地点を格納（ここが現在地点）
　　現在地点から、次に行こうと思えば行けるポイントを全部探し出す
    for 地点 in 次に行こうと思えば行けるポイント
        if その地点は既に「探索済みリスト」にある？
            探索済みなので「探索候補スタック」には入れない（continue）
        if その地点は既に「探索候補スタック」にある？（閉路があるなら可能性あり、木なら可能性なし）
            探索予定なので「探索候補スタック」には入れない（continue）
        未探索かつ候補にも入っていない地点なので「探索候補スタック」に追加する（append）
print 探索済み地点
"""

from collections import deque

[H, W] = [int(i) for i in input().split()]
S = [list(input()) for _ in range(H)]
[sy, sx] = [0, 0]

#sの位置の特定＞＞特定したらsx、syに代入
for i in range(H):
    for j in range(W):
        if S[i][j] == 's':
            [sy, sx] = [i, j]

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(sy, sx):
    reached = [[0] * W for _ in range(H)]
    #内包表記。W,H=5,4の場合、reaced = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    #つまり全て0のW,Hフィールドを用意している
    que = deque([[sy, sx]])
    reached[sy][sx] = 1
    #スタート地点をqueに登録
    #出発点を1にしている

    while que:
        [y, x] = que.pop()
        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if yy < 0 or xx < 0 or yy > H - 1 or xx > W - 1 or S[yy][xx] == '#' or reached[yy][xx] != 0:
                continue
            else:
                if S[yy][xx] == 'g':
                    return True
                reached[yy][xx] = 1
                que.append([yy, xx])
    return False


if dfs(sy, sx):
    print("Yes")
else:
    print("No")



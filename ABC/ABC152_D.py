
#参考：http://at274.hatenablog.com/entry/2020/01/24/060000

N = int(input())
# cnt[i][j] := 先頭がi, 末尾がjで始まるような数
# 個数を格納できる行列の準備
cnt = [[0] * 10 for i in range(10)]
# Nまでカウントする（11>(1,1) 10231>(1,1))
for n in range(1, N + 1):
    cnt[int(str(n)[0])][int(str(n)[-1])] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += cnt[i][j] * cnt[j][i]

print(ans)
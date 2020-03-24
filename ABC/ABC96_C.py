import sys

H,W = map(int,input().split())
s = [list(input()) for i in range(H)]
a = [["."]*W for _ in range(H)]
for i in range(H):
    for j in range(1,W):
        if s[i][j-1] == "#" and s[i][j] == "#":
            a[i][j-1] = "#"
            a[i][j] = "#"

sT = list(zip(*s))
aT = [list(x) for x in zip(*a)]

for i in range(W):
    for j in range(1,H):
        if sT[i][j-1] == "#" and sT[i][j] == "#":
            aT[i][j-1] = "#"
            aT[i][j] = "#"

ans = list(zip(*aT))

for i in range(H):
    for j in range(W):
        if s[i][j] != ans[i][j]:
            print("No")
            sys.exit()
print("Yes")
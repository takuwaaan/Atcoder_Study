N = int(input())
H = list(map(int, input().split()))
th = H[0]
f = True
for i in range(1, N):
    if th <= H[i]:
        th = H[i]
    if H[i] < th - 1:
        f = False
        break
if f:
    print("Yes")
else:
    print("No")

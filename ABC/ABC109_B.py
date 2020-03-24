N = int(input())
tell = []
f = True
last = ""
for i in range(N):
    W = input()
    if i != 0 and W[0] != last:
        f = False
        break
    elif i != 0 and W in tell:
        f = False
        break
    last = W[-1]
    tell.append(W)
if f:
    print("Yes")
else:
    print("No")


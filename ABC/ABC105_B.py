N = int(input())
f = False
for i in range(N//4+1):
    for j in range(N//7+1):
        if i*4 + j*7 == N:
            f = True
            break
if f:
    print("Yes")
else:
    print("No")
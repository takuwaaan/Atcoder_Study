a = [0] * 3
for i in range(3):
    a[i] = list(map(int, input().split()))
N = int(input())
b = [0] * N
for i in range(N):
    b[i] = int(input())

for i in range(N):
    for j in range(3):
        for k in range(3):
            if a[j][k] == b[i]:
                a[j][k] = 0
if sum(a[0]) == 0 or sum(a[1]) == 0 or sum(a[2]) == 0:
    print("Yes")
elif a[0][0] + a[1][1] + a[2][2] == 0 or a[0][2] + a[1][1] + a[2][0] == 0:
    print("Yes")
elif a[0][0] + a[1][0] + a[2][0] == 0 or a[0][1] + a[1][1] + a[2][1] == 0 or a[0][2] + a[1][2] + a[2][2] == 0:
    print("Yes")
else:
    print("No")

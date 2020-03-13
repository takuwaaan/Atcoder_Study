N = int(input())
p = list(map(int,input().split()))
count = 0
F = True
for i in range(0,N):
    if p[i] != i+1:
        count += 1
    if count == 3:
        F = False
        break
if F:
    print("YES")
else:
    print("NO")


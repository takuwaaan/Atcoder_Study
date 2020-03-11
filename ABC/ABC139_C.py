N = int(input())
H = list(map(int, input().split()))
ans = 0
count = []
for i in range(N - 1):
    if H[i] - H[i + 1] >= 0:
        ans += 1
        count.append(ans)
    if H[i] - H[i + 1] < 0:
        ans = 0
count.sort()
if count:
    print(count[-1])
else:
    print(0)
n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
    if p[i + 2] > p[i + 1] > p[i] or p[i + 2] < p[i + 1] < p[i]:
        ans += 1
print(ans)

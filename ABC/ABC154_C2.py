n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = "YES"
for i in range(1, n):
    if a[i] == a[i - 1]:
        ans = "NO"
        break
print(ans)

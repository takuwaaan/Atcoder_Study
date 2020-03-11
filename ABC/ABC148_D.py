n = int(input())
a = list(map(int, input().split()))

count = 0
c = 1
for i in range(n):
    if a[i] == c:
        c += 1
    else:
        count += 1
if count == n:
    print(-1)
else:
    print(count)

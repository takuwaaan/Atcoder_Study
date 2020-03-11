N = int(input())
d = list(map(int, input().split()))
count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        count += d[i] * d[j]
print(count)

import bisect

N = int(input())
L = list(map(int, input().split()))
L.sort()
count = 0
for a in range(N):
    for b in range(a + 1, N):
        c = bisect.bisect_left(L, L[a] + L[b])
        if c > b:
            count += c - b - 1
        else:
            break
print(count)

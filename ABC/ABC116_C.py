N = int(input())
h = list(map(int,input().split()))
count = 0
i = 0
while sum(h) > 0:
    if h[i] > 0:
        j = i
        count += 1
        while j < N and h[j] > 0:
            h[j] = h[j] - 1
            j += 1
    else:
        i += 1
print(count)
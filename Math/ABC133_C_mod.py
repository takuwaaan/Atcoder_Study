L, R = map(int, input().split())
mod = 2019
ans = mod + 1

if R - L >= 3000 or L == 0:
    print(0)
else:
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            m = ((i % mod) * (j % mod)) % mod
            if m < ans:
                ans = m
    print(ans)

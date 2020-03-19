N = int(input())
ans = 0
for _ in range(N):
    x, u = input().split()
    x = float(x)
    if u == "BTC":
        ans += x * 380000.0
    else:
        ans += x
print(ans)

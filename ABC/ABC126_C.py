N,K = map(int,input().split())
ans = 0
for i in range(1,N+1):
    if i >= K:
        ans += 1/N
        continue
    for n in range(1,1000000):
        i *= 2
        if i >= K:
            ans += (1 / N) * (0.5 ** n)
            break
print(ans)

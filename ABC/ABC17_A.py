ans = 0
for _ in range(3):
    s,e = map(int,input().split())
    ans += s*(e*0.1)
print(int(ans))
n,k,m = map(int,input().split())
a = list(map(int,input().split()))

x = m*(n)-sum(a)

if x <= k:
    if x < 0:
        print(0)
    else:
        print(x)
else:
    print(-1)

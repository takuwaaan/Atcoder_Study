X,Y = map(int,input().split())
count = X
for i in range(1,10**18):
    count *= 2
    print(count)
    if count >= Y:
        print(i)
        break
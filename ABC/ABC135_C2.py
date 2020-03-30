n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split())) + [0]
c = [0] * (n + 1)

cnt = 0
for i in range(n + 1):
    print("###")
    print(a,b,c)
    if a[i] <= b[i] + c[i]:
        cnt += a[i]
        b[i] -= max(0, a[i] - c[i])
        if i < n:
            c[i + 1] = b[i]
    else:
        cnt += b[i] + c[i]
    print(a,b,c)
    print("###")
print(cnt)

N = int(input())
res = []
for i in range(N):
    name, price = input().split()
    index = i + 1
    res.append([index, name, int(price)])

res.sort(key=lambda x: x[2], reverse=True)
res.sort(key=lambda x: x[1])

for i in range(N):
    print(res[i][0])

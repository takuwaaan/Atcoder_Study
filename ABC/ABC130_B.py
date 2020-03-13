N,X = map(int,input().split())
L = list(map(int,input().split()))
count = 1
s = 0
for i in range(N):
    s += L[i]
    if s <= X:
        count += 1
print(count)

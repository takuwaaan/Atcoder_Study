import sys

N = int(input())
a = [0]
for _ in range(N):
    a.append(int(input()))
s = 1
for i in range(N):
    tmp = a[s]
    if tmp == 2:
        print(i+1)
        sys.exit()
    else:
        s = tmp
print(-1)

l = list(map(int,input().split()))
K = int(input())
l.sort()
for _ in range(K):
    l[-1] *= 2
print(sum(l))

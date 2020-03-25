N = int(input())
X = list(map(int,input().split()))
s_X = sorted(X)
c = s_X[-(N//2)]
c2 = s_X[-(N//2)-1]

for i in range(N):
    if X[i] < c:
        print(c)
    else:
        print(c2)
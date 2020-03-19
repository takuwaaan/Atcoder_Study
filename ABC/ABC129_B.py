N = int(input())
W = list(map(int,input().split()))
L_count = 0
R_count = 0
div = 100000
s = sum(W)
for i in range(N):
    L_count += W[i]
    R_count = s - L_count
    d = abs(L_count-R_count)
    if div > d:
        div = d
print(div)



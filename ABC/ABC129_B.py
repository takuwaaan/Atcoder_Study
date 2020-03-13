import math

N = int(input())
W = list(map(int,input().split()))
s = sum(W)
count = 0
for i in range(N):
    count += W[i]
    if count >= s/2 and i < N-1:
        print(abs(2*count - s))
        break
    elif i == N-1:
        count -= W[-1]
        print(abs(count - W[-1]))
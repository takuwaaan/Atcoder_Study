N,S,T = map(int,input().split())
W = int(input())

count = 1 if S<=W<=T else 0
for _ in range(N-1):
    a = int(input())
    W += a
    if S<=W<=T:
        count+=1
print(count)
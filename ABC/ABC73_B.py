N = int(input())
count = 0
for _ in range(N):
    l,r = map(int,input().split())
    count += r-l+1
print(count)
N = int(input())
K = int(input())
x = list(map(int,input().split()))
count = 0
for i in range(N):
    count += min(x[i]*2,abs(x[i]-K)*2)
print(count)
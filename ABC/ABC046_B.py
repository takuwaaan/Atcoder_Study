n,k = map(int,input().split())
s = k
while(n>1):
    s *= (k-1)
    n-=1
print(s)
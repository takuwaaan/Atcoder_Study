import collections

n,k=map(int,input().split())
a=list(map(int,input().split()))

ca = collections.Counter(a)
lk = ca.most_common(k)
print(lk)
sk = sum([lk[i][1] for i in range(len(lk))])
print(n-sk)

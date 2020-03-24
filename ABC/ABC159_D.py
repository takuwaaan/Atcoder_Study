import collections

N = int(input())
A = list(map(int,input().split()))
a = collections.Counter(A)
v = a.values()
l_v = list(v)

#合計
s = 0
for i in range(len(l_v)):
    n = l_v[i]-1
    s += n*(n+1)//2
#カウント
for i in range(N):
    print(s-(a[A[i]]-1))

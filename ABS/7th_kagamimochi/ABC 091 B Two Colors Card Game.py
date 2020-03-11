import collections

n=int(input())
s=[]
for i in range(n):
    s.append(input())
m=int(input())
t=[]
for i in range(m):
    t.append(input())
sc = collections.Counter(s)
tc = collections.Counter(t)

for i in range(n):
    for j in range(t):
        if s[i] == j[i]:

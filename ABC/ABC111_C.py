import collections

n = int(input())
v = list(map(int,input().split()))
a = []
b = []
for i in range(n):
    if i%2 == 0:
        a.append(v[i])
    else:
        b.append(v[i])
ac = collections.Counter(a)
bc = collections.Counter(b)
ac_max = ac.most_common()
bc_max = bc.most_common()
mm = max(ac_max[0][1],bc_max[0][1])

if ac_max[0][0] == bc_max[0][0]:
    m2 =
    print(n - mm - )
import collections

n = int(input())
s = []
for i in range(n):
    s.append(input())
c = collections.Counter(s)
c_most = c.most_common()

i = 0
ans = []
while (True):
    ans.append(c_most[i][0])
#    print(c_most[i][0])
    i += 1
    if i == len(c_most):
        break
    if c_most[i][1] != c_most[i - 1][1]:
        break
ans.sort()
for i in range(len(ans)):
    print(ans[i])
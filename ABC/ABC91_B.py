s = []
t = []
N = int(input())
for _ in range(N):
    s.append(input())
M = int(input())
for _ in range(M):
    t.append(input())
s_set = set(s)
s_list = list(s_set)
c = []
count = 0
for i in range(len(s_list)):
    for j in range(len(s)):
        if s_list[i] == s[j]:
            count += 1
    for k in range(len(t)):
        if s_list[i] == t[k]:
            count -= 1
    c.append(count)
    count = 0
ans = max(c)
if ans > 0:
    print(ans)
else:
    print(0)
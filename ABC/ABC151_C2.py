from collections import defaultdict

N,M = map(int,input().split())
AC_dict = defaultdict(int)
ans_AC = 0
ans_WA = 0

for _ in range(M):
    p,s = input().split()
    p = int(p)
    if s == "AC":
        if AC_dict[p] == -1:
            continue
        else:
            ans_AC += 1
            ans_WA += AC_dict[p]
            AC_dict[p] = -1
    else:
        if AC_dict[p] == -1:
            continue
        else:
            AC_dict[p] += 1

print(ans_AC,ans_WA)
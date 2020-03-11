##https://atcoder.jp/contests/abc079/tasks/abc079_c

s = input()
n = 3
l = ["+", "-"]
# bit全探索
for i in range(2 ** n):
    pm = []
    tmp = ""
    ans = int(s[0])
    for j in range(n):
        if ((i >> j) & 1):
            pm.append(l[0])
        else:
            pm.append(l[1])
    for k in range(n):
        if pm[k] == "+":
            ans += int(s[k + 1])
        else:
            ans -= int(s[k + 1])
    if ans == 7:
        print(s[0]+pm[0]+s[1]+pm[1]+s[2]+pm[2]+s[3]+"=7")
        break
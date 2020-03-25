s=input()
a = []
for i in range(len(s)):
    if s[i] == "0":
        a.append("0")
    elif s[i] == "1":
        a.append("1")
    elif s[i] == "B":
        if len(a) == 0:
            continue
        else:
            a.pop(-1)
ans = ""
for i in range(len(a)):
    ans += a[i]
print(ans)
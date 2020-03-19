s = int(input())
a = []
ans = 1
while s not in a:
    a.append(s)
    ans += 1
    if s % 2 == 0:
        s = s // 2
    else:
        s = 3 * s + 1
print(ans)

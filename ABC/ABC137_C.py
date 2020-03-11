N = int(input())
count = 0
ans = 0
s = [""] * N
for i in range(N):
    tmp = sorted(input())
    s[i] = "".join(tmp)
s.sort()
for i in range(N - 1):
    if s[i] == s[i + 1]:
        count += 1
    elif s[i] != s[i + 1] and count > 0:
        ans += count * (count + 1) // 2
        count = 0
if count > 0:
    ans += count * (count + 1) // 2
    count = 0
print(ans)

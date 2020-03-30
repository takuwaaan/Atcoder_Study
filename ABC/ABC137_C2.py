N = int(input())
s = [""]*N
for i in range(N):
    tmp = list(input())
    tmp.sort()
    s[i] = "".join(tmp)
s.sort()
cnt = 0
ans = 0
for i in range(1,N):
    if s[i-1] == s[i]:
        cnt += 1
    else:
        ans += (cnt*(cnt+1))//2
        cnt = 0
ans += (cnt*(cnt+1))//2
print(ans)
s = input()
ans = ""
for i,word in enumerate(s):
    if i%2 == 0:
        ans += s[i]
    else:
        continue
print(ans)
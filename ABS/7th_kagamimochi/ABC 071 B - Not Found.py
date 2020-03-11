s = input()
alfa = [chr(i) for i in range(97, 97+26)]
for i in range(len(alfa)):
    for j in range(len(s)):
        if alfa[i] == s[j]:
            alfa[i] = "-"
for i in range(len(alfa)):
    if alfa[i] != "-":
        ans = alfa[i]
        break
    else:
        ans = "None"
print(ans)
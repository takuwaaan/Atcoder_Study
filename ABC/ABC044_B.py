w = input()
alfa = [chr(i) for i in range(97, 97+26)]
s = [0]*len(alfa)
for i in range(len(w)):
    for j in range(len(alfa)):
        if w[i]==alfa[j]:
            s[j]+=1

ans = True
for i in range(len(s)):
    if s[i]%2 != 0:
        ans = False
if(ans):
    print("Yes")
else:
    print("No")

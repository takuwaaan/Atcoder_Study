S = input()
K = int(input())

div = 0
for i in range(len(S)):
    if S[i] != "1":
        div = i
        break

if div >= K:
    print(1)
else:
    print(S[div])
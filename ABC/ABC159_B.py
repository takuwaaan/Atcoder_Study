S = input()
N = len(S)
f = True

for i in range(N):
    if S[i] != S[N-i-1]:
        f = False
        break

N2 = (N-1)//2
for i in range(N2):
    if S[i] != S[N2-i-1]:
        f = False
        break

N3 = (N+3)//2
for i in range(N3,N):
    if S[i] != S[N-i-1]:
        f = False
        break
if f:
    print("Yes")
else:
    print("No")
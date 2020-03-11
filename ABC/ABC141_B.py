S = list(input())
f = True
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == "L":
            f = False
    elif i % 2 != 0:
        if S[i] == "R":
            f = False
if f:
    print("Yes")
else:
    print("No")
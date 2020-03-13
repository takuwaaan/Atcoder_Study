S = list(input())
f = True
for i in range(3):
    if S[i] == S[i+1]:
        f = False
        break
if f:
    print("Good")
else:
    print("Bad")

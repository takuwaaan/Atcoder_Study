import sys
S = input()
SL = list(S)
N = len(S)

if S[0] != "A":
    print("WA")
    sys.exit()

if S[2:-1].count("C") != 1:
    print("WA")
    sys.exit()

SL[0] = "a"
for i in range(2,N-1):
    if SL[i] == "C":
        SL[i] = "c"
        break
S2 = "".join(SL)
if not S2.islower():
    print("WA")
    sys.exit()
print("AC")

S = input()
LL = int(S[0] + S[1])
RR = int(S[2] + S[3])
# YY or MM
L = ""
if LL == 0 or LL > 12:
    L = "YY"
else:
    L = "YY or MM"

if L == "YY":
    if RR == 0 or RR > 12:
        print("NA")
    elif 1 <= RR <= 12:
        print("YYMM")
elif L == "YY or MM":
    if RR == 0 or RR > 12:
        print("MMYY")
    elif 1 <= RR <= 12:
        print("AMBIGUOUS")

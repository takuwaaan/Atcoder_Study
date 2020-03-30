import sys

A, B = map(int, input().split())
S = input()
l = ["0","1","2","3","4","5","6","7","8","9"]
if S[A] != "-":
    print("No")
    sys.exit()
for i in range(len(S)):
    if i == A:
        continue
    elif S[i] not in l:
        print("No")
        sys.exit()
print("Yes")
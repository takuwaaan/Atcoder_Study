import sys

A,B,C = map(int,input().split())
for i in range(0,A*B+1,A):
    if i == 0:
        continue
    if i % B == C:
        print("YES")
        sys.exit()
print("NO")
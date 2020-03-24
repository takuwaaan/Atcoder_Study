N = int(input())
SN = str(N)
count = 0
for i in range(len(SN)):
    count += int(SN[i])
if N % count == 0:
    print("Yes")
else:
    print("No")
import math
h=int(input())
s=int(math.log2(h))
ans = 0
if s == 0:
    print(1)
else:
    for i in range(1,s+1):
        ans += 2**i
    print(ans+1)

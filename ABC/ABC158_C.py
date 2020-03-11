import math

A,B = map(int,input().split())
tmp_Bx = B * 10

f = False
for i in range(tmp_Bx,tmp_Bx+10):
    Ax = math.floor(0.08 * i)
    if Ax == A:
        print(i)
        f = True
        break
if f == False:
    print(-1)
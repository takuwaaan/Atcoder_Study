N,A,B = map(int,input().split())
loop = N // (A+B)
extra = N - loop*(A+B)
if extra >= A:
    print(loop * A + A)
else:
    print(loop * A + extra)

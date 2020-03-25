A,B,C,X,Y = map(int,input().split())
count = 0
if A >= C*2 or B >= C*2:
    print(max(X,Y)*2*C)

elif A+B >= C*2:
    if X > Y:
        print(Y*2*C + (X-Y)*A)
    elif X < Y:
        print(X*2*C + (Y-X)*B)
    else:
        print(X*2*C)
else:
    print(X*A+Y*B)

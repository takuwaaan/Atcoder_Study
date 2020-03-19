A,B = map(int,input().split())
if abs(A-B) >= 2:
    print(max(A,B)*2-1)
else:
    print(A+B)
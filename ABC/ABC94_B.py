N,M,X = map(int,input().split())
A = list(map(int,input().split()))
L_c = 0
R_c = 0
for i in range(M):
    if A[i]<X:
        L_c+=1
    elif A[i]>X:
        R_c+=1
print(min(L_c,R_c))
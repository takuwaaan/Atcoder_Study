N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())
tmp = sorted(A)
m1 = tmp[-1]
m2 = tmp[-2]
for i in range(N):
    if A[i] != m1:
        print(m1)
    else:
        print(m2)

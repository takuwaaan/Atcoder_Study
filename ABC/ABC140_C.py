N = int(input())
B = list(map(int, input().split()))
A = [-1] * N
B_sort = sorted(B)
for i in range(N - 1):
    index = B.index(B_sort[i])
    if A[index] == -1:
        A[index] = B[index]
    else:
        A[index] = min(A[index], B[index])
    if A[index + 1] == -1:
        A[index + 1] = B[index]
    else:
        A[index + 1] = min(A[index + 1], B[index])
    B[index] = -1
print(sum(A))

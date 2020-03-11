N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
st = 0
for i in range(N):
    st += B[A[i] - 1]
    if i >= 1 and A[i] == A[i - 1] + 1:
        st += C[A[i] - 2]
print(st)

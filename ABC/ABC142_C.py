N = int(input())
A = list(map(int, input().split()))
R = [0] * N
for i in range(N):
    R[A[i] - 1] = i + 1
print(*R)

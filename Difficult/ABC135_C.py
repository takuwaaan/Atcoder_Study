#????????????

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.append(0)
C = [0] * (N + 2)

cnt = 0

for i in range(N + 1):
    if A[i] <= B[i] + C[i]:
        cnt += A[i]
        C[i + 1] = B[i] - max(0, A[i] - C[i])
    else:
        cnt += B[i] + C[i]

print(cnt)

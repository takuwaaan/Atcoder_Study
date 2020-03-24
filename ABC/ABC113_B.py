N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
count = 10 ** 9
ans = 0
for i in range(N):
    aveT = abs(A - (T - 0.006 * H[i]))
    if count >= aveT:
        count = aveT
        ans = i + 1
print(ans)

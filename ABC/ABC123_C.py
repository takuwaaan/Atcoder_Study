import math

N = int(input())
T = [0] * 5
for i in range(5):
    T[i] = int(input())
ans = math.ceil(N / min(T)) + 4
print(ans)
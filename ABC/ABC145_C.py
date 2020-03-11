import math

N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())


def dist(x1, y1, x2, y2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d


route = 0
for i in range(N):
    for j in range(i + 1, N):
        route+=dist(x[i], y[i], x[j], y[j])
ave = (route * (2 * math.factorial(N - 1))) / math.factorial(N)
print(ave)

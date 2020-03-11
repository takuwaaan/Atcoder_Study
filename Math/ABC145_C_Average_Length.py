import math

N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())


def dist(x1, y1, x2, y2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d

"""
次の問題を考えます.
• N 個の互いに区別出来るボールを 1 列に並べる. 特定の 2 つのボールが隣り合うような並べ方
は何通りあるか.
「特定の 2 つのボール」を一纏めにして考えて, この 2 つのボールの並び順も考慮すると, この問題の
答えは 2 (N − 1)! 通りであることが分かります.
これより, 元の問題における N! 通りの経路において, 各町のペア間の移動が発生するような経路は,
2 (N − 1)! 個であることが分かります.
"""

route = 0
for i in range(N):
    for j in range(i + 1, N):
        route+=dist(x[i], y[i], x[j], y[j])
ave = (route * (2 * math.factorial(N - 1))) / math.factorial(N)
print(ave)

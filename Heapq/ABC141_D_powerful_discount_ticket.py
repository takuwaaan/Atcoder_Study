# https://qiita.com/ell/items/fe52a9eb9499b7060ed6

import heapq
import sys

input = sys.stdin.readline


def main():

    N, M = map(int, input().split())
    A = list(map(lambda x: int(x) * (-1), input().split()))
    heapq.heapify(A)

    for _ in range(M):
        tmp = heapq.heappop(A)
        tmp *= -1
        tmp = tmp // 2
        heapq.heappush(A, tmp * (-1))
    print(sum(A) * (-1))


if __name__ == '__main__':
    main()

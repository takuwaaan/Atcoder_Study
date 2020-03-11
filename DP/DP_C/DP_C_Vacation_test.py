# 参考：https://atcoder.jp/contests/dp/submissions/7930399
# 定形、inputより速度10倍程度速い
import sys

input = sys.stdin.readline


# 関数化した方が高速？
def main():
    N = int(input())
    a1, b1, c1 = 0, 0, 0
    for _ in range(N):
        a, b, c = map(int, input().split())
        a0, b0, c0 = a1, b1, c1
        a1 = a + max(b0, c0)
        # 元文：a1 = a + (b0 if b0 > c0 else c0)
        b1 = b + max(a0, c0)
        c1 = c + max(a0, b0)

    print(max(a1, b1, c1))


if __name__ == '__main__':
    main()

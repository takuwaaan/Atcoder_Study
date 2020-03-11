# https://atcoder.jp/contests/dp/tasks/dp_b
#関数化するとちょっと早くなる...(今回関数化しないとTLE）
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    h = [int(x) for x in input().split()]

    dp = [0] * (N)
    dp[0] = 0

    # 参考：https://atcoder.jp/contests/dp/submissions/10181844
    for i in range(1, N):
        tmp = [dp[k] + abs(h[i] - h[k]) for k in range(max(0, i - K), i)]
        dp[i] = min(tmp)
    print(dp[-1])

if __name__ == '__main__':
    main()

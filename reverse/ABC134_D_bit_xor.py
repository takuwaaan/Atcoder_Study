#参考：https://atcoder.jp/contests/abc134/submissions/6458463
#bitを使わない 逆から考える
n = int(input())
arr = list(map(int, input().split()))

res = [0] * (n + 1)

for i in range(1, n + 1)[::-1]:
    sum_res = sum(res[x] for x in range(i, n + 1, i))
    if sum_res % 2 != arr[i - 1]:
        res[i] = 1

print(sum(res))

if sum(res):
    ans = []
    for i, ele in enumerate(res):
        if ele:
            ans.append(i)
    print(*ans)

###
#https://ami-atcoder.hatenablog.com/entry/20190724/1563947653
import sys
def input():
    return sys.stdin.readline().rstrip()
def main():
    n = int(input())
    bits = [int(e) for e in input().split()]
    ans = set()
    for i in reversed(range(n)):
        for j in range(i + (i + 1), n, i + 1):
            bits[i] ^= bits[j]
        if bits[i] == 1:
            ans.add(i + 1)
    print(len(ans))
    print(*ans)
main()

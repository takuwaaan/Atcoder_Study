#参考：https://atcoder.jp/contests/abc134/submissions/6458463

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

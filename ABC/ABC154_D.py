n, k = map(int, input().split())
p = list(map(int, input().split()))

tmp_sum = sum(p[0:k])
ans = (tmp_sum + k) / 2
count = float(0)
for i in range(k, n):
    tmp_sum = tmp_sum + p[i] - p[i - k]
    tmp = (tmp_sum + k) / 2
    if ans <= tmp:
        ans = tmp

print(ans)

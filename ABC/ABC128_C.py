n, m = map(int, input().split())

kss = [list(map(int, input().split())) for _ in range(m)]

p = list(map(int, input().split()))

cnt = 0

for i in range(2 ** n):
    bin_i = '{:010b}'.format(i)[::-1]

    for i in range(m):
        ks = kss[i]
        k = ks[0]
        s = ks[1:]

        sum_s = 0

        for j in range(k):
            sum_s += int(bin_i[s[j]-1])

        if sum_s % 2 != p[i]:
            break
    else:
        cnt += 1

print(cnt)

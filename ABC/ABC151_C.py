n, m = map(int, input().split())
p = [""] * m
for i in range(m):
    p[i] = input().split()
    p[i][0] = int(p[i][0])

print(p)

ac = [0] * n
wa = [0] * n

for i in range(m):
    if p[i][1] == "AC":
        ac[p[i][0] - 1] = 1
    if p[i][1] == "WA":
        if ac[p[i][0] - 1] == 1:
            continue
        else:
            wa[p[i][0] - 1] += 1
print(sum(ac), sum(wa))

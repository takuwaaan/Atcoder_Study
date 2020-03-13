P = list(map(int,input().split()))
ans = []
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        ans.append(P[i]+P[j])
ans.sort()
print(ans[0])

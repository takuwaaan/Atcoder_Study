A,B,K = map(int,input().split())
ans = []
for i in range(A,K+A):
    if i > B:
        break
    ans.append(i)

for i in range(B-K+1,B+1):
    if i < A:
        continue
    ans.append(i)

ans = set(ans)
ans = list(ans)
ans.sort()
for i in range(len(ans)):
    print(ans[i])
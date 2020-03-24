N = int(input())
S = list(input())
ans = []
for i in range(1,N):
    a = set(S[:i])
    b = set(S[i:])
    ans.append(len(a&b))
print(max(ans))
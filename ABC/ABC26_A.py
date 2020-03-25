A = int(input())
ans = []
for i in range(1,A+1):
    ans.append(i*(A-i))
ans.sort()
print(ans[-1])
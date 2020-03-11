N = int(input())
A = list(map(lambda x: int(x) ** (-1), input().split()))
ans = 1 / sum(A)
print(ans)
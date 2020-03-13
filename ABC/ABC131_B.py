N, L = map(int, input().split())
applepye = 0
eat = 0
if N + L <= 0:
    eat = L + N - 1
    for i in range(L, L + N):
        applepye += i
    print(applepye - eat)
elif N + L > 0 and L >= 0:
    eat = L
    for i in range(L, L + N):
        applepye += i
    print(applepye - eat)
else:
    eat = 0
    for i in range(L, L + N):
        applepye += i
    print(applepye - eat)

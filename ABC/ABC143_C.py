from collections import deque

N = int(input())
S = deque(list(input()))
count = 1
if len(S) == 1:
    print(1)
else:
    q = S.popleft()
    while (True):
        if q != S[0]:
            count += 1
        q = S.popleft()
        if len(S) == 0:
            break
    print(count)

S = input()
N =len(S)
cnt = 0

if N == 1:
    print(0)
else:
    for i in range(1,N):
        if S[i-1] != S[i]:
            cnt+= 1
    print(cnt)
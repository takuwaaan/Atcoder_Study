S = input()
ans = 1000
for i in range(len(S)-2):
    tmp = abs(753-int(S[i]+S[i+1]+S[i+2]))
    if ans > tmp:
        ans = tmp
print(ans)
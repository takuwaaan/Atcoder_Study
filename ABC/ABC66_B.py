S = input()
N =len(S)
for i in reversed(range(2,N,2)):
    l = i//2
#    print(l,i)
#    print(S[:l],S[l:i])
    if S[:l] == S[l:i]:
        print(len(S[:i]))
        break

N = int(input())
S = input()
s = S[1:].count("E")
ans = [s]
for i in range(1,N):
    if S[i-1] == "W":
        s += 1
    if S[i] == "E":
        s -= 1
    ans.append(s)
print(min(ans))


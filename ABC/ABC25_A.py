S = input()
N = int(input())
l = []
for i in range(5):
    for j in range(5):
        l.append(S[i]+S[j])
l.sort()
print(l[N-1])
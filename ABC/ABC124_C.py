S = input()
N = len(S)
count_f1 = 0
count_f0 = 0
#101010
for i in range(N):
    if i % 2 == 0 and S[i] != "1":
        count_f1 += 1
    elif i % 2 == 1 and S[i] != "0":
        count_f1 += 1

for i in range(N):
    if i % 2 == 0 and S[i] != "0":
        count_f0 += 1
    elif i % 2 == 1 and S[i] != "1":
        count_f0 += 1

print(min(count_f1,count_f0))



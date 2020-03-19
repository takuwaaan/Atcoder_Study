S = input()
count_1 = 0
count_0 = 0
for i in range(len(S)):
    if S[i] == "1":
        count_1 += 1
    else:
        count_0 += 1
print(count_0 + count_1 - abs(count_0 - count_1))

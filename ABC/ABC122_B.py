S = input()
count = 0
c = [0]
for i in range(len(S)):
    if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
        count += 1
    else:
        c.append(count)
        count = 0
c.append(count)
print(max(c))
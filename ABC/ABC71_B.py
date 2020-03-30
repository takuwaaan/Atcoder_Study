import sys

S = input()
alfa = [chr(i) for i in range(97, 97+26)]
l = [0] * 26

for i in range(len(S)):
    index = alfa.index(S[i])
    l[index] += 1

for i in range(len(l)):
    if l[i] == 0:
        print(alfa[i])
        sys.exit()
print("None")

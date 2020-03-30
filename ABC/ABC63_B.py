import sys

S = input()
l = [0]*26
alfa = [chr(i) for i in range(97, 97+26)]
for i in range(len(S)):
    index = alfa.index(S[i])
    l[index] += 1
    if l[index] == 2:
        print("no")
        sys.exit()
print("yes")
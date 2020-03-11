n=int(input())
s=input()
alfa = [chr(i) for i in range(65,65+26)]
ans = []
for i in range(len(s)):
    tmp = alfa.index(s[i])+n
    if tmp >= 26:
        tmp -= 26
    print(alfa[tmp],end="")
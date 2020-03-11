alpha2num = lambda c: ord(c) - ord('A') + 1
c = input()
ans = alpha2num(c)+1
num2alpha = lambda c: chr(c+64)
print(num2alpha(ans))
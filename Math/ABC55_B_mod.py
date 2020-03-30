N = int(input())
p = 1
mod = 10 ** 9 + 7
for i in range(1,N + 1):
    p = (p*i) % mod
print(p)

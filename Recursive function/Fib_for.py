#https://qiita.com/drken/items/23a4f604fa3f505dd5ad#fnref1

N = int(input())
f = [0] * 10000
f[0] = 0
f[1] = 1
for i in range(2, N):
    f[i] = f[i - 1] + f[i - 2]
print(f[N-1])
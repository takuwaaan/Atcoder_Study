#https://qiita.com/drken/items/23a4f604fa3f505dd5ad#fnref1

def Fib(n):
    if n <=1:
        return 1
    return Fib(n-1)+Fib(n-2)

N = int(input())
ans = Fib(N)
print(ans)
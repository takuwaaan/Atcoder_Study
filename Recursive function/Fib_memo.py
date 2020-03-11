# https://qiita.com/drken/items/23a4f604fa3f505dd5ad#fnref1

def fib_memo(n):
    """メモ化フィボナッチ"""
    memo = [0]*(n+1)

    def _fib(n):
        if n <= 1:
            return n
        if memo[n] != 0:
            return memo[n]
        memo[n] = _fib(n-1) + _fib(n-2)
        return memo[n]

    return _fib(n)

N = int(input())
print(fib_memo(N))
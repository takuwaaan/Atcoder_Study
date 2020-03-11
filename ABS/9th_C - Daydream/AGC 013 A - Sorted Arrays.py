n = int(input())
a = list(map(int,input().split()))

def plus_minus(a,b,judge):
    if a < b:
        judge = True
    elif a > b:
        judge = False
    return judge

for i in range(n-1):
    if s
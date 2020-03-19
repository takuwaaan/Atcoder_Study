# 公約数列挙
# 重複する約数は1つにまとまるので注意
def make_common_divisors(x1, x2):
    cd = [1]
    for i in range(2, min(x1, x2) + 1):
        if x1 % i == 0 and x2 % i == 0:
            cd.append(i)
    return cd

A,B,K = map(int,input().split())
print(make_common_divisors(A,B)[-K])
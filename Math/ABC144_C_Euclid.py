#N = int(input())

a = 1112
b = 695

#約数列挙
#重複する約数は1つにまとまるので注意
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

print(make_divisors(a))

# 最大公約数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(gcd(a, b))


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


print(lcm(a, b))
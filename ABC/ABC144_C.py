N = int(input())

#約数列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

yaku = make_divisors(N)
if len(yaku) % 2 != 0:
    ans = yaku[-1]*2 - 2
    print(ans)
else:
    ans = yaku[-1] + yaku[-2] -2
    print(ans)
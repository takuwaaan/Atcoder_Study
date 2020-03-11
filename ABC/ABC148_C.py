a,b = map(int,input().split())
def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a
print(a*b//gcd(a,b))
import sys
a,b = input().split()
s = int(a+b)
for i in range(1,10000):
    if s / i == i:
        print("Yes")
        sys.exit()
print("No")
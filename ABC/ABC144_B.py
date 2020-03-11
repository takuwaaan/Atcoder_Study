N = int(input())
f = False
for i in range(1, 10):
    if N % i != 0:
        continue
    else:
        if N / i > 9:
            continue
        else:
            f = True
if f:
    print("Yes")
else:
    print("No")

n = int(input())
a =list(map(int,input().split()))
f = True
for i in range(n):
    if a[i] % 2 != 0:
        continue
    if a[i] % 2 == 0:
        if a[i] % 3 == 0 or a[i] % 5 == 0:
            continue
        else:
            f = False
            break
if f == False:
    print("DENIED")
if f == True:
    print("APPROVED")

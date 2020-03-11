n = int(input())
flag = False
for i in range(int(n/4)+1):
    for j in range(int(n/7)+1):
        if i==0 and j==0:
            continue
        if n%((4*i)+(7*j)) == 0:
            flag = True
            break
if flag:
    print("Yes")
else:
    print("No")
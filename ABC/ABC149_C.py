import math
x = int(input())
f = True
ans = True
while(f):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            ans = False
            break
        elif x % i !=0:
            ans = True
    if ans == True:
        print(x)
        f=False
    elif ans == False:
        x+=1
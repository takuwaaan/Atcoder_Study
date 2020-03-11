a,b = map(int,input().split())
ave = (a+b)/2
if ave%1 != 0:
    print(int(ave+1))
else:
    print(int(ave))
a,b,k=map(int,input().split())
if a-k>0 and a+b > k:
    print(str(a-k)+" "+str(b))
elif a-k <= 0 and a+b > k:
    print(str(0)+" "+str(b-(a-k)*(-1)))
else:
    print(str(0)+" "+str(0))

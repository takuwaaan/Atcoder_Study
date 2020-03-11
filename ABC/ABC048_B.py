a,b,x = map(int,input().split())
ans=0
if a>0:
    ans = b//x-(a-1)//x
elif a==0:
    ans = b//x+1
print(ans)
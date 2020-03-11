a,b,c,x,y=map(int,input().split())
s = []
for i in range(max(x,y)+1):
    xs=x-i
    ys=y-i
    if xs <= 0:
        xs=0
    if ys <= 0:
        ys=0
    s.append(a*xs+b*ys+c*2*i)
print(min(s))
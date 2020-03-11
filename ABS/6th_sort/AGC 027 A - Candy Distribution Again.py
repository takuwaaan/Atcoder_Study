n,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
s = [0]*n
c = 0
for i in range(n):
    s[i]+=a[i]
    x=x-a[i]
    if x<0:
        break
    if s[i] == a[i]:
        c+=1

if x>0:
    c-=1
print(c)
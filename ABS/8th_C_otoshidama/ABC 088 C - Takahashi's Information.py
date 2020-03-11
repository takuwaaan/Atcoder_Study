c1 = list(map(int,input().split()))
c2 = list(map(int,input().split()))
c3 = list(map(int,input().split()))

ans = True
a1=0
b=[]
for i in range(3):
    b.append(c1[i]-a1)

a2=c2[0]-b[0]
a3=c3[0]-b[0]

for i in range(1,3):
    if a2+b[i] != c2[i] or a3+b[i] != c3[i]:
        ans = False
        break

if ans==True:
    print("Yes")
else:
    print("No")

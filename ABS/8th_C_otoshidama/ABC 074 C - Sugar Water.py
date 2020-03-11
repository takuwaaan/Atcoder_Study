a,b,c,d,e,f=map(int,input().split())
a=100*a
b=200*b

water = min(a,b)
sugar_list = []
sugar = 0
i=0
j=0
while(True):
    while(True):
        sugar = c*i+d+j
        sugar_list.append(sugar)
        j+=1
        if sugar > e:
            sugar=0
            break
    i+=1
    if sugar > e:
        break

m_sugar = max(sugar_list)
s = water + m_sugar
print(s)
print(m_sugar)
print(sugar_list)

"""
100 200 10 20 15 200
a = min(100,200) = 100
<=15
b = max(10,20) = 10
s = 110

100 200 1 2 100 1000
a = min(100,200) =100
<=100
b = max(1,2)=100
s = 110

****

mizu=[]
for k in range(2):
    for l in range(2):
        if a*k+b*l+min(c,d)>f:
            continue
        mizu.append(a*k+b+l)

s_mizu=[]
for i in range(2):
    for j in range(2):
        if c*i+d*j>e:
            continue
        for k in range(len(mizu)):
            s_mizu.append(100*(c*i+d+j)/(mizu[k]+c*i+b*j))

print(mizu)
print(s_mizu)
"""
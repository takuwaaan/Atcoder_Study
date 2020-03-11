n=int(input())

def keta(x):
    k = 0
    while(x>0):
        k+=1
        x = int(x/10)
    return k

s=[]
for i in range(1,int(n**0.5)+1):
    if n%i != 0:
        continue
    b=n/i
    f_ab=max(keta(i),keta(b))
    s.append(f_ab)
print(min(s))

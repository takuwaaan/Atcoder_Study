a,b = map(int,input().split())
c = 0
for i in range(a,b+1):
    s = str(i)
    if s == s[::-1]:
        c+=1
print(c)


"""
以下ではTLEとなった
def digit10_str(n):
    dten_str = ""
    while(n>0):
        dten_str+=str(n%10)
        n/=10
    return dten_str

a,b = map(int,input().split())
c = 0
for i in range(a,b+1):
    if digit10_str(i)[0]==digit10_str(i)[-1] and digit10_str(i)[1]==digit10_str(i)[-2]:
        c+=1
print(c)
"""
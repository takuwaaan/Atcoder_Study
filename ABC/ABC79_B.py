N = int(input())
l = [2,1]
for i in range(1,N):
    l.append(l[i]+l[i-1])
print(l[-1])
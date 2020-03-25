A = int(input())
B = int(input())
C = int(input())
a = [A,B,C]
l = [A,B,C]
l.sort(reverse=True)
for i in range(3):
    print(l.index(a[i])+1)
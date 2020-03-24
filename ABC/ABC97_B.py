X = int(input())
b = [1]
for i in range(2, 100):
    for j in range(2,100):
        b.append(i**j)
b.sort()
for i in range(1,len(b)):
    if b[i] > X:
        print(b[i-1])
        break
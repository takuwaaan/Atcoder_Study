antena = [0] * 5
for i in range(5):
    antena[i] = int(input())
antena.sort()
k = int(input())
if antena[-1] - antena[0] > k:
    print(":(")
else:
    print("Yay!")
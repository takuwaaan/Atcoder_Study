A, B = map(int, input().split())
for i in range(100):
    if i >= (B - 1) / (A - 1):
        print(i)
        break

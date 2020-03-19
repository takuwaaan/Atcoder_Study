N, M = map(int, input().split())
AB = []
for i in range(N):
    A, B = map(int, input().split())
    AB.append([A, B])
AB.sort(key=lambda x: x[0])
count = 0
money = 0
for i in range(N):
    count += AB[i][1]
    money += AB[i][0] * AB[i][1]
    if count >= M:
        money -= (count - M) * AB[i][0]
        break
print(money)

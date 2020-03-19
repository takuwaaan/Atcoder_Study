import math

menu = []
score = 0
ans = 0
for i in range(5):
    m = int(input())
    score = m % 10
    if score == 0:
        score = 10
    menu.append([m, score])

menu.sort(key=lambda x: x[1], reverse=True)

for i in range(5):
    if i < 4:
        tmp = math.ceil(menu[i][0] / 10) * 10
    else:
        tmp = menu[i][0]
    ans += int(tmp)
print(ans)

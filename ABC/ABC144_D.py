import math

a, b, x = map(int, input().split())
s_all = (a ** 2) * b
if x <= s_all / 2:
    tmp = (a * b ** 2) / (2 * x)
    tan = math.atan(tmp)
else:
    tmp = 2 * (s_all - x) / (a ** 3)
    tan = math.atan(tmp)
print(math.degrees(tan))

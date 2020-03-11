a, b = map(int, input().split())
sa = ""
sb = ""
for i in range(b):
    sa+=str(a)
for i in range(a):
    sb+=str(b)
if sa>sb:
    print(sb)
elif sa<sb:
    print(sa)
else:
    print(sa)
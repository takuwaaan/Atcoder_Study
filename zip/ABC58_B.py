O = input()
E = input()
ans = ""
if len(O) > len(E):
    for i in range(len(E)):
        ans += O[i]+E[i]
    print(ans + O[-1])
elif len(O) < len(E):
    for i in range(len(O)):
        ans += O[i]+E[i]
    print(ans + E[-1])
else:
    for i in range(len(O)):
        ans += O[i]+E[i]
    print(ans)

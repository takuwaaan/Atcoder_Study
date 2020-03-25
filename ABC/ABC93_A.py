S = list(input())
S.sort()
a = "".join(S)
print("Yes" if a == "abc" else "No")

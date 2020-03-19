N = int(input())
L = list(map(int,input().split()))
L.sort()
s = sum(L) - L[-1]
if L[-1] < s:
    print("Yes")
else:
    print("No")
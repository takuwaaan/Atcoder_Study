N = int(input())
S = list(input().split())
S_set = set(S)
l = len(S_set)
print("Three" if l == 3 else "Four")
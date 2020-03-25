A, B = map(int, input().split())
if (B != 1 and A > B) or (A == 1 and B != 1):
    print("Alice")
elif (A != 1 and A < B) or (B == 1 and A != 1):
    print("Bob")
else:
    print("Draw")

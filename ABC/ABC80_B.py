S = input()
N = int(S)
fn = 0
for i in range(len(S)):
    fn += int(S[i])
print("Yes" if N % fn == 0 else "No")
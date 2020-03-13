#参考：https://takeg.hatenadiary.jp/entry/2019/09/14/132409

S = input()
N = len(S)
ans = [0] * N

#R
count = 0
for i in range(N):
    if S[i] == "R":
        count += 1
    else:
        ans[i] += count // 2
        ans[i-1] += count - (count // 2)
        count = 0
#L
count = 0
for i in reversed(range(0,N)):
    if S[i] == "L":
        count += 1
    else:
        ans[i+1] += count - (count // 2)
        ans[i] += count // 2
        count = 0

answer = ' '.join(map(str, ans))
print(answer)


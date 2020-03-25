h,w = map(int,input().split())
s = [input() for _ in range(h)]
ans=[]
for i in range(h):
    ans.append(s[i])
    ans.append(s[i])
for i in range(h*2):
    print(ans[i])
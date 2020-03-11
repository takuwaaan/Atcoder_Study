n = int(input())
ans = list(range(n+1))
for i in ans:
    if ans[i]%2!=0:
        ans[i]=0
    else:
        count = 0
        while(True):
            if ans[i]%2 != 0 or ans[i] == 0:
                ans[i] = count
                break
            else:
                ans[i]/=2
                count+=1
ans[0] = -1
print(ans.index(max(ans)))
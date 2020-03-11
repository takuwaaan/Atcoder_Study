n=int(input())+3
s=input()+"ZZZ"
ans = ""
c=0
for i in range(n-2):
    ans += s[i]+s[i+1]+s[i+2]
    if ans == "ABC":
        c+=1
    ans = ""
print(c)
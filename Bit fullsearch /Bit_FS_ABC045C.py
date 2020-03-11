#https://atcoder.jp/contests/arc061/tasks/arc061_a

s=input()
n=len(s)-1
l=["+",""]
sum = 0

#1桁ならそのまま出力
if len(s) < 2:
    sum = s

#bit全探索
else:
    for i in range(2 ** n):
        #plusは”+”か””を格納
        plus = []
        tmp = ""
        ans = 0
        #パターン抽出("+" "" "" とか "" "+" ""とかを順番に）
        for j in range(n):
            if ((i>>j) & 1):
                plus.append(l[0])
            else:
                plus.append(l[1])
        #sを一個一個取り出し、+か""を結合 12+5 とか 1+25の文字列ができる
        for i in range(n):
            tmp += s[i]+plus[i]
            if i == n-1:
                tmp+=s[i+1]
        #+でsplitする 12+5 > "12" "5"
        #intに直して加算
        tmp2 = tmp.split("+")
        for i in range(len(tmp2)):
            ans += int(tmp2[i])
        #合計に加えていく
        sum+=ans

print(sum)


#https://atcoder.jp/contests/panasonic2020/submissions/10900296

import decimal
a,b,c = map(decimal.Decimal,input().split())
roota = decimal.Decimal.sqrt(a)
rootb = decimal.Decimal.sqrt(b)
rootc = decimal.Decimal.sqrt(c)
if roota + rootb < rootc:
  print("Yes")
else:
  print("No")

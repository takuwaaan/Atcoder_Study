#https://qiita.com/_-_-_-_-_/items/89e966df1c1764f70690
#bisect_leftメソッドは昇順ソートされたリストに昇順を崩さず挿入できる位置を返します。　

import bisect
a=[1,3,5,7,9,11,13,15,17,19]
x=4

insert_index = bisect.bisect_left(a,x)

"""
insert_index=2
"""

a.insert(insert_index,x)

print(a)
"""
Out[1]:[1,3,4,5,7,9,11,13,15,17,19]
"""
#https://qiita.com/_-_-_-_-_/items/89e966df1c1764f70690

a=[1,1,1,1,2,2,2,2,3,3,3,3]
x=2

import bisect
insert_index = bisect.bisect_left(a,x)
a.insert(insert_index,x)
print(insert_index)
print(a)
"""
Out[1]: 4
[1,1,1,1,2,2,2,2,3,3,3,3]
         ^
"""

a=[1,1,1,1,2,2,2,2,3,3,3,3]
x=2

insert_index2 = bisect.bisect_right(a,x)
a.insert(insert_index2,x)
print(insert_index2)
print(a)
"""
Out[2]: 8
[1,1,1,1,2,2,2,2,3,3,3,3]
                 ^
"""

#bisect.insert_left(a,x)
"""
[1,1,1,1,2,2,2,2,2,3,3,3,3]
         ^
"""
#bisect.insert_right(a,x)
#bisect.insert(a,x)
"""
[1,1,1,1,2,2,2,2,2,3,3,3,3]
                 ^
"""
# coding: utf-8


import collections 


aa = ("홍길동", 21, "남")
bb = ("강복녀", 23, "여")

for n in [aa, bb]:
    print('%s, %d, %s' %n)


Person = collections.namedtuple("Person", 'name age gender')

aa = Person(name="홍길동", age="25", gender="남")
bb = Person(name="강길녀", age="21", gender="여")

for n in [aa, bb]:
    print('%s는 %s세, %s입니다.' %n)

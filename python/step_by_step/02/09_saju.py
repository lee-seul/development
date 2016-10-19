# coding: utf-8

y, m, d = map(int, input().split())

if str(y+m+d)[-1] == '0':
    print(u"운수대통!")
else:
    print(u"노력하세요!")



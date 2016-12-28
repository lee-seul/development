# coding: utf-8

import collections

dic = {}

dic["서울"] = "LG트윈스"
dic["대구"] = "삼성라이온즈"
dic["광주"] = "기아타이거즈"

for i, j in dic.items():
    print(i, j)

# 자료의 순서를 기억하는 사전형 클래스

dic1 = collections.OrderedDict()
dic1["서울"] = "LG트윈스"
dic1["대구"] = "삼성라이온즈"
dic1["광주"] = "기아타이거즈"

for i,j in dic1.items():
    print(i, j)

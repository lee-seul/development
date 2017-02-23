# coding: utf-8

record = u"lee2619910824대구"
birth = slice(5, 9)
name = slice(0, 3)

print(record[birth])
print(record[name])

code = "2011 2014 2015 2009 1999 2017 2012 2010"
scode = slice(0, 10, 2)
print(code[scode])

record1 = "고길동1501012341234서울"
print(name.indices(len(record1)))



# coding: utf-8

def outer_func(tag):
    #message = 'hi'
    #text = 'Some text'
    tag = tag

    def inner_func(txt):
        #print(message)
        text = txt
        print('<{0}>{1}<{0}>'.format(tag, text))

    #return inner_func()
    return inner_func

h1_func = outer_func('h1')
p_func = outer_func('p')

h1_func(u'h1 태그 안입니다.')
p_func(u'p 태그 안입니다.')

#my_func = outer_func()

#my_func()

#print(my_func)
#print()
#print(dir(my_func))
#print()
#print(type(my_func.__closure__))
#print()
#print(my_func.__closure__)
#print()
#print(my_func.__closure__[0])
#print()
#print(dir(my_func.__closure__[0]))
#print()
#print(my_func.__closure__[0].cell_contents)



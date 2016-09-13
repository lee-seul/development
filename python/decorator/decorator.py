# coding: utf-8

"""def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()
"""

#def decorator_function(original_function):
#    def wrapper_function(*args, **kwargs):
#        print('{} 함수가 호출되기 전입니다.'.format(original_function.__name__))
#        return original_function(*args, **kwargs)
#    return wrapper_function

class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(u'{} 함수가 호출되기 전입니다.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@DecoratorClass
def display():
    print(u'display 함수가 실행되었습니다.')

@DecoratorClass
def display_info(name, age):
    print(u'display_info({}, {}) 함수가 실행되었습니다.'.format(name, age))

#display_1 = decorator_fuction(display_1)
#display_2 = decorator_fuction(display_2)

display()
print()
display_info('john', 25)



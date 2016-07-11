# coding: utf-8
# user_defined_exception.py

# 사용자 정의 예외 만들기
class TooBigNumError(Exception):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return 'Too big number {}. Use 1~10!.'.foramt(self.val)

# 예외처리 시험 함수 
def user_defined_exception_test():
    num = int(input('1부터 10사이의 정수를 입력하세요! : '))
    if num > 10:
        raise TooBigNumError(num)
    print('숫자 {}를 입력하셨군요!'.format(num))


user_defined_exception_test()

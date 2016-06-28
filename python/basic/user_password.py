# coding: utf-8
# user_password.py

import re

def password_validation_check(pwd):
    """ checking password validation

    Args:
        pwd (str) : password string

    Return:
        True or False (boolean) : the result of checking validation

    """
    # 비밀번호 확인(6~12)
    if len(pwd) < 6 or len(pwd) > 12:
        print(pwd, "의 길이가 적당하지 않습니다")
        return False
    
    # 숫자 혹은 알파벳 유무 확인
    if re.findall('[a-zA-Z0-9]+', pwd)[0] != pwd:
        print(pwd, '는 숫자와 영문자로만 구성되지 않았습니다.')
        return False
    
    # 알파벳 대소문자 확인 
    if len(re.findall('[a-z]', pwd)) == 0 or len(re.findall('[A-Z]', pwd)) == 0:
        print(pwd, "는 영문 대문자와 소문자가 함께 존재하지 않습니다.")
        return False

    print(pwd, "는 비밀번호로 적당합니다!")
    return True


if __name__ == '__main__' :
    password_validation_check('24dfd')
    password_validation_check('423423423423424f')
    password_validation_check('1231213')
    password_validation_check('123asds1213')



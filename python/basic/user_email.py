# coding: utf-8
# user_email.py

import re

def email_validation_check(email):
    """ checking email address validation

        Args:
            email (str) : e-mail address string

        Return:
            True or False (boolean) : the result of checking validation
    """
    # 이메일 주소 정합성 유무 확인
    if re.findall(r'[\w.-]+@[\w.-]+.\w+', email)[0] != email:
        print(email, "는 이메일 주소로 적당하지 않습니다!")
        return False
    
    print(email, "는 이메일 주소로 적당합니다!")
    return True



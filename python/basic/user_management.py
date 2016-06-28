# coding: utf-8
# user_management.py

import user_email as ue
import user_password as upr 

class User:
    """This class keeping user's email address and password

    Put email address & password when creating instance.
    And also need to check validation of address & password.
    
    """
    # 초기화 함수 재정의
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd
        self.check_validation()

    # 정합성 검증 함수 호출을 통한 이메일 주소 및 비밀번호 적합성 검증
    def check_validation(self):
        """checking email & password validation
        """
        ue.email_validation_check(self.email)
        upr.password_validation_check(self.pwd)

if __name__ == '__main__':
    user1 = User('isi.cho@gmail.com', 'dsf23Afd')
    print("========================================")

    user2 = User('isi.cho@gmail*c0m', 'eee')
    print("========================================")

    user3 = User('i#i.cho@gmail*c0m', 'eeesdfA233!!')


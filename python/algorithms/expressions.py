# coding: utf-8
# expressions.py

# 숫자의 표현

def expressions(num):
    answer = 0
    value = 1
    while(value!=num+1):
        total = 0
        for i in range(value, num+1):
            total += i  
            if total == num:
                answer += 1 
                value += 1
                break
            elif total > num:
                value += 1
                break
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15));


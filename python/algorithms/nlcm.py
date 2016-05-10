# coding: utf-8
# nlcm.py
# N개의 최소 공배수

# 최대 공약수 
def gcb(a,b):
    if a % b == 0:        
        return b  
    return gcb(b, a%b)

# 최소 공배수
def lcm(a,b):
    return int(a*b/gcb(a,b))

def nlcm(num):
    answer = num[0]
    for i in range(1,len(num)):
        answer = (lcm(answer, num[i]))
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));

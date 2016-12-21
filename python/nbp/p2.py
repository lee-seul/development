# coding: utf-8

"""
# d가 1자리 수일때, short coding
def solution(n, d):
    return str(list(range(1, n+1))).count(str(d))


# 단순한 방법, 자리수와 상관 없음
def count_number(n, d):
    result = 0
    d = str(d)
    for i in range(1, n+1):
        result += str(i).count(d)
    return result
"""


# 규칙성 활용, 재귀함수
def solution(n, d):
    if n < 0 or d < 0:
        return -1
    digit = len(str(n)) - 1  # floor(log(n, 10))
    first = int(str(n)[0])  # n의 첫째 자리수
    result = 0
    if d == 0:
        for i in range(digit-1):  # 1, 10, 100, 1000
            result += 9 * 10 ** i * (i+1)
        for j in range(first-1):  # 2, 3, 4, 5 ...
            result += 10**(digit-1) * digit
        for k in range(10**digit*first, n+1):  # 나머지
            result += str(k).count(str(d))
        return result
    else:
        if digit == 0:  # 재귀 종료
            if n >= d:
                result += 1
            return result
        n -= 10**digit * first
        result = 10**(digit-1) * digit * first  # 각 자리수까지 계산
        if first == d:
            result += n
            if n == 0:
                result += 1
                return result
        elif first > d:
            result += 10**(digit)
        result += solution(n, d)
        return result


if __name__ == '__main__':
    while True:
        n, d = map(int, input().split())
        print(solution(n, d))

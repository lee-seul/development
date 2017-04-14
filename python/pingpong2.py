# coding: utf-8

def having_seven(c):
    if not c: 
        return False
    
    if not (c-7) % 10: 
        return True
    return having_seven(c//10) 


def seven(c, plus): 
    if not c % 7 or having_seven(c): 
        return plus * (-1)
    return plus


def get_pingpong(x, n, c, plus):
    if x == c:
        return n
    return get_pingpong(x, n+seven(c, plus), c+1, seven(c, plus))


def pingpong(x):
    return get_pingpong(x, 1, 1, 1) # 초기 값을 설정해준다.


print(pingpong(int(input())))


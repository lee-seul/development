# coding: utf-8


def in_seven(c):
    if not c:
        return False
    if not (c - 7) % 10:
        return True
    return in_seven(c//10)


def is_seven(c, plus):
    if not c % 7 or in_seven(c):
        return plus * -1
    return plus


def get_pingpong(x, n, c, plus):
    if x == c:
        return n
    return get_pingpong(x, n + is_seven(c, plus), c + 1, is_seven(c ,plus))


def pingpong(x):
    return get_pingpong(x, 1, 1, 1)


print(pingpong(int(input())))


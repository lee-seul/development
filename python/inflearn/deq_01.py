# coding: utf-8

from collections import deque

dQ = deque(maxlen = 4)

dQ.append('aa')
dQ.append('bb')
dQ.append('cc')
dQ.append('dd')

def search_word(lines, find_word, histroy = 4):
    previous_lines = deque(maxlen=histroy)
    for readline in lines:
        if find_word in readline:
            yield readline, previous_lines
        previous_lines.append(readline)

with open('someText.txt') as f:
    fword = search_word(f, "aa")
    print(next(fword))

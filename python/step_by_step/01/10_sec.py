# coding: utf-8

def sec():
    a = int(input())
    day = a//86400
    hour = (a-day*86400)//3600
    minute = (a-day*86400 - hour*3600)//60
    sec = a-day*86400 - hour*3600 - minute * 60
    print(day, hour, minute, sec)

sec()


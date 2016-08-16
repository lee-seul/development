# coding: utf-8

from os import listdir, rename

def changeFileName():
    """
    파일 이름을 변경하는 함수
    """
    files = listdir('.')
    for name in files:
        if name.startswith('01_'):
            newname = name[4:]
            rename(name, newname)
            print(name , "=>", newname)

changeFileName()

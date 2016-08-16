# coding: utf-8

def change():
    a = str(1000 - int(input()))
    print(int(a[0]), int(a[1])//5, (int(a[1])-(int(a[1])//5*5)))

change()

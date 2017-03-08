# coding: utf-8

class Singletone(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singletone, cls).__new__(cls)
        return cls.instance


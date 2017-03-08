# coding: utf-8

from airforce import AirForce

class Bomber(AirForce):
    def __init__(self, bomb_num):
        self._bomb_num = bomb_num

    def take_off(self):
        print(u"폭격기 발진")

    def fly(self):
        print(u"폭격기 출격")

    def attack(self):
        for i in range(self._bomb_num):
            print(u"폭탄 투하")
            self._bomb_num = self._bomb_num - 1

    def land(self):
        print(u"폭격기 착륙")


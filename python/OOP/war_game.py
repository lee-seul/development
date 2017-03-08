# coding: utf-8

from fighter import Fighter
from bomber import Bomb
import airforce

def war_game(airforce):
    airforce.take_off()
    airforce.fly()
    airforce.attack()
    airforce.land()

if __name__ == '__main__':
    f15 = Fighter(3)
    war_game(f15)
    print()

    b29 = Bomb(3)
    war_game(b29)



# coding: utf-8

class Subsystem1:
    def play(self):
        pass

class Subsystem2:
    def stop(self):
        pass

class Subsystem3:
    def pause(self):
        pass



class Facade:
    def __init__(self):
        self.one = Subsystem1()
        self.two = Subsystem2()
        self.three = Subsystem3()

    def exec(self):
        self.one.play()
        self.three.pause()
        self.two.stop()


if __name__ == "__main__":
    f = Facade()
    f.exec()



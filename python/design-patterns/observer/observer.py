# coding: utf-8

class Observer:
    def __init__(self):
        self.subscriber = []
        self.msg = ""

    def notify(self):
        for sub in self.subscriber:
            sub.msg = self.msg

    def register(self, obsv):
        self.subscriber.append(obsv)

    def unregister(self, obsv):
        self.subscriber.remove(obsv)


class subscriber:
    def __init__(self):
        msg = ""

    def update(self):
        print(self.msg)


class Subject:
    def __init__(self):
        self.observer = []

    def notify_observer(self, info):
        for obsv in self.observer:
            obsv.msg = info

    def attach(self, obsv):
        self.observer.append(obsv)

    def dettach(self, obsv):
        self.observer.remove(obsv)


if __name__ == "__main__":
    a = subscriber()
    b = subscriber()
    c = subscriber()
    
    ob = Observer()
    ob.register(a)
    ob.register(b)
    ob.register(c)

    sub = Subject()
    sub.attach(ob)
    
    sub.notify_observer("Hello")

    ob.notify()
    
    a.update()
    b.update()
    c.update()

    


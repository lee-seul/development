# coding: utf-8

class Message(object):
    def __init__(self, msg):
        self.text = msg

    def printmsg(self):
        print(self.text)

l = []

for i in range(1, 11):
    text = chr(i + 64) * 5
    m = Message("#{} {}".format(i, text))
    l.append(m)

for msg in l:
    msg.printmsg()


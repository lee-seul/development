# coding: utf-8

class Person(object):
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.lastname + " " + self.firstname


class Employee(Person):
    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum

    def __str__(self):
        return super().__str__() + ", " + self.staffnumber

x = Person("M", "S")
y = Employee("H", "S", "108")

print(x)
print(y)



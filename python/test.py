class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone


class Student(Person):
    def __init__(self, name, phone, major, stu_no):
        super().__init__(self, name, phone)
        self.major = major
        self.stu_no = stu_no

    def get_major(self):
        return self.major
    
    def get_no(self):
        return self.stu_no
    

class Worker(Person):
    def __init__(self, name, phone, part, worker_no):
        super().__init__(self, name, phone)
        self.part = part
        self.worker_no = worker_no
    
    def get_part(self):
        return self.part

    def get_no(self):
        return self.worker_no
    

class Address(Student, Worker):
    def __init__(self, name, phone, mp, sw, ss):
        Worker.__init__(self, name, phone, mp, sw)
        Student.__init__(self, name, phone, mp, sw)
        self.job = ss

    def get_info(self):
        if(self.job == 'S'):
            print("Student: {0}\t{1}\t{2}\t{3}\t{4}").format(self.name, self.phone, self.major, self.stu_no)
        elif(self.job == 'W'):
            print("Worker: {0}\t{1}\t{2}\t{3}\t{4}").format(self.name, self.phone, self.part, self.worker_no)


a = Address('jiho', '1234', '전공', '1234', 'S')
b = Address('jiosdjf', '34235', 'sdlfkj', '123r52435', 'W')
print("asdfadsf")
a.get_info()
b.get_info()

class Student:
    def __init__(self):
        self.sname = "Abhishek"
        self.dob = self.Dob()

    def display(self):
        print("The name of the student is : ", self.sname)

    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 8
            self.yy = 96

        def display(self):
            print("The DOB is {}/{}/{}".format(self.dd, self.mm, self.yy))


p = Student()
p.display()
x = p.dob
x.display()

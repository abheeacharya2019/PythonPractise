class Employee:

    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self):
        print("Emplyee no is : ", self.eno)
        print("Employee name is : ", self.ename)
        print("Employee salary is : ", self.esal)


class Test:
    def modify(emp):
        emp.esal = emp.esal + 500
        emp.display()


e = Employee(1, "Abhishek", 10000)
Test.modify(e)

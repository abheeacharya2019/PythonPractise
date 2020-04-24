class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def display(self):
        print("MY car {} is a {} color car..".format(self.model, self.color))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print("Eat Piza and drink beer and code python..")


class Employee(Person):
    def __init__(self, name, age, eno, esal, car):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
        self.car = car

    def work(self):
        print("Python coding is my life....")

    def empInfo(self):
        print("Employee Name is : ", self.name)
        print("Employee age is : ", self.age)
        print("Employee no is : ", self.eno)
        print("Salery is :", self.esal)
        print("The car info is : ")
        self.car.display()


c1 = Car("BMW i8", "red")
e1 = Employee("Abhishek", 24, 100, 1000, c1)
e1.eatndrink()
e1.work()
e1.empInfo()



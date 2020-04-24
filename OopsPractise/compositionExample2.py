class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print("My {} car of model {} with color {} is really soo good.".format(self.name, self.model, self.color))


class Employee:
    def __init__(self, name, company, car):
        self.name = name
        self.company = company
        self.car = car

    def empInfo(self):
        print("Name of the employee is :", self.name)
        print("Name of the company is :", self.company)
        print("Car info : ")
        self.car.getinfo()


c = Car("MG", "hactor", "Red")
e = Employee("Abhishek", "GS", c)
e.empInfo()

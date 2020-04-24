class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatnDrink(self):
        print("Eat pizaa and drink beer")


class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def work(self):
        print("Coding python is very easy like drinking chilled beer")

    def empInfo(self):
        print("name of the employee :", self.name)
        print("Employee Age :", self.age)
        print("Employee no :", self.eno)
        print("Emplotee salary :", self.esal)


e = Employee("Durga", 48, 100, 10000)
e.eatnDrink()
e.work()
e.empInfo()
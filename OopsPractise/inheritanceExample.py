class Parent:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        print("This is a parent m1 method")

    @classmethod
    def m2(cls):
        print("this is a class method..")

    @staticmethod
    def m3():
        print("This is a static method..")


class Child(Parent):
    pass


c = Child()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()

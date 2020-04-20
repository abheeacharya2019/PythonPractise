class Test:
    a = 10  # This is a static variable

    def __init__(self):
        print(self.a)
        print(Test.a)

    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print(Test.a)
        print(cls.a)

    @staticmethod
    def m3():
        print(Test.a)


t = Test()
print(Test.a)
print(t.a)
t.m1()
t.m2()
t.m3()
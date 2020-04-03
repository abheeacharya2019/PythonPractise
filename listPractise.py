class Test:
    a = 10

    def __init__(self):
        Test.b = 20

    def m1(self):
        Test.c = 30

    @classmethod
    def m2(cls):
        Test.d = 40
        cls.e = 50

    @staticmethod
    def m3():
        Test.f = 60


print(Test.__dict__)
t = Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.a = 80
print(Test.__dict__)

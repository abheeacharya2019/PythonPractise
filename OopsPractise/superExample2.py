class P:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        print("This is m1 method of parent")

    @classmethod
    def m2(cls):
        print("This is m2 class method of parent")

    @staticmethod
    def m3():
        print("This is m3 static method of Parent")


class C(P):
    a = 888

    def __init__(self):
        self.b = 999
        super().__init__()
        print(super(C, self).a)
        super().m1()
        super().m2()
        super(C, self).m3()


c = C()
print(c.a)
print(c.b)

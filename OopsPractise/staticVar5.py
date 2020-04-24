class Test:
    a = 10

    def __init__(self):
        self.b = 20


t1 = Test()
t2 = Test()
Test.a = 888
t1.b = 999
print(t1.a, t1.b)
print(t2.a, t2.b)

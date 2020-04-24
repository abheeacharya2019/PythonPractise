class Outer:
    def __init__(self):
        print("This is a outer class..")

    class Inner:
        def __init__(self):
            print("This is a inner class...")

        def m1(self):
            print("This is a inner class method...")


o = Outer()
i = o.Inner()
i.m1()
